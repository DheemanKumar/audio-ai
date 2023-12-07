import os
import csv
from pydub import AudioSegment
import os

path = os.path.dirname(os.path.abspath(__file__))
os.chdir(path)

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

csv_file = os.path.join(path,"unprocessed_audio_data.csv")
csv_file2 = os.path.join(path,"broken_3s_audio_data.csv")

language=["english","hindi","punjabi","bangoli","noise"]


def get_sample():
    oldnames=os.listdir("newaudio")
    for n in range(len(oldnames)):
        if(oldnames[n] != "note"):
            return os.path.join(path,"newaudio",oldnames[n])


get_sample()

def execute(noise,g,l):

    # set file path
    

    if(noise!=1):
        l=5


    data = []
    #print(noise," ",g," ",l)
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
            os.rename("newaudio/"+oldnames[n],"unbroken_audio/"+language[l-1] +" audio sample "+str(index+n)+".wav")


    # adding new audifile names to list "data"

    names=os.listdir("unbroken_audio") 
    #names=os.listdir("newaudio") 




    for i in names:
        if(i != "note"):
            score=[i,0,0,0,0,0,0,0]
            
            if (noise==2):
                score[7]=1
            else:
                if (g==1):
                    score[1]=1
                else:
                    score[2]=1
                if (l==1):
                    score[3]=1
                elif (l==2):
                    score[4]=1
                elif (l==3):
                    score[5]=1
                else:
                    score[6]=1
            
            data.append(score)







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
            input_file = os.path.join(path,"unbroken_audio",i)
            output_folder = os.path.join(path,"3sec_audio")

            if not os.path.exists(output_folder):
                os.makedirs(output_folder)
            segment_duration = 3  # in seconds

            #print(i)
            Aaudio=split_audio(input_file, output_folder, segment_duration,len(os.listdir(output_folder)),language[l-1], start_from_end=False)
            #print(Aaudio)
            Aaudio+=split_audio(input_file, output_folder, segment_duration,len(os.listdir(output_folder)),language[l-1], start_from_end=True)

            variables=[]
            
            for j in data:
                if(j[0]==i):
                    #print(j)
                    variables=j

            for j in Aaudio:
                bdata.append([j]+variables+[0])
            
            #print(Aaudio)

            
            
            

            os.rename(input_file,os.path.join(path,"broken_audio",i))
        #print()



    with open(csv_file2, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(bheader)  # Write the header row
        writer.writerows(bdata)    
            


#print(names)