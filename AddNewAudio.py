import os
import csv
from pydub import AudioSegment
import os

def split_audio(input_file, output_folder, segment_duration,index,hedder, start_from_end=False):
    audio = AudioSegment.from_wav(input_file)
    total_duration = len(audio)
    segment_length = segment_duration * 1000  # Convert to milliseconds

    audio_data=[]

    if start_from_end:
        start_times = list(range(total_duration, 0, -segment_length))
    else:
        start_times = list(range(0, total_duration, segment_length))

    for i, start_time in enumerate(start_times):
        end_time = min(start_time + segment_length, total_duration)
        segment = audio[start_time:end_time]
        
        if(segment.duration_seconds==3):
            segment.export(os.path.join(output_folder, f"{hedder}_sample_{i+index + 1}.wav"), format="wav")
            audio_data.append(f"{hedder}_sample_{i+index + 1}.wav")
    
    return audio_data




language="hindi"
csv_file = language+"_unprocessed_audio_data.csv"
csv_file2 = language+"_broken_3s_audio_data.csv"

data = []

#open unprocessed_audio_data and storing that in list "data" also making header
try :
    with open(csv_file, mode="r") as file:
        reader = csv.reader(file)
        header = next(reader)  # Read the header row
        for row in reader:
            data.append(row)

except:
    header=["name","male","female","english","hindi","punjabi","bangoli","noise"]
    



oldnames=os.listdir("newaudio")     # storing all new audio files name in "names"
#print(oldnames)
# renaming new audio files
index=len(data)
for n in range(len(oldnames)):
    if(oldnames[n] != "note"):
         os.rename("newaudio/"+oldnames[n],"unbroken_audio/"+language +" audio sample "+str(index+n)+".wav")


# adding new audifile names to list "data"
names=os.listdir("unbroken_audio") 

for i in names:
    if(i != "note"):
         data.append([i,1,0,0,1,0,0,0])




# Writing data to CSV file unprocessed_audio_data
with open(csv_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(header)  # Write the header row
    writer.writerows(data)


bdata=[]  #broken data


# open broken_3s_audio_data and storing that in list "bdata" 
try :
    with open(csv_file2, mode="r") as file:
        reader = csv.reader(file)
        bheader = next(reader)  # Read the header row
        for row in reader:
            bdata.append(row)

except:
    bheader=["name","old name","male","female","english","hindi","punjabi","bangoli","noise","check"]


# braking all audio files in new audio in section of 3 sec and storing that data in 3sec_audio
#print(names)
for i in names:
    if(i != "note"):
        input_file = f"/Users/dheemankumar/Desktop/FILE/audio-ai/unbroken_audio/{i}"
    
        output_folder = "/Users/dheemankumar/Desktop/FILE/audio-ai/3sec_audio"
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        segment_duration = 3  # in seconds

        print(i)
        Aaudio=split_audio(input_file, output_folder, segment_duration,len(os.listdir(output_folder)),language, start_from_end=False)
        #print(Aaudio)
        Aaudio+=split_audio(input_file, output_folder, segment_duration,len(os.listdir(output_folder)),language, start_from_end=True)

        variables=[]
        
        for j in data:
            if(j[0]==i):
                #print(j)
                variables=j

        for j in Aaudio:
            bdata.append([j]+variables+[0])
        
        #print(Aaudio)

        
        
        

        os.rename(input_file,f"/Users/dheemankumar/Desktop/FILE/audio-ai/broken_audio/{i}")
    #print()



with open(csv_file2, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(bheader)  # Write the header row
    writer.writerows(bdata)    
           




#print(names)