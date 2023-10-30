import csv

# CSV file path
language="hindi"
csv_file =language+"_broken_3s_audio_data.csv"
header=[]

# Read data from CSV file
data = []
with open(csv_file, mode="r") as file:
    reader = csv.reader(file)
    header = next(reader)  # Read the header row
    for row in reader:
        data.append(row)



def savedata(Data=data, Header=header, csv_file=language+"_broken_3s_audio_data.csv"):
    with open(csv_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(Header)  # Write the header row
        writer.writerows(Data)    # Write the updated data


def updatedata(index:int,given_data:dict):
    data[index][2]=int(given_data["male"])
    data[index][3]=int(given_data["female"])
    data[index][4]=int(given_data["english"])
    data[index][5]=int(given_data["hindi"])
    data[index][6]=int(given_data["punjabi"])
    data[index][7]=int(given_data["bangoli"])
    data[index][8]=int(given_data["noise"])
    data[index][9]=int(given_data["check"])


def dict2list():
    pass

def list2dict(data:list) ->dict:
    if len(data)!=10:
        return FileNotFoundError
    ans={"name":data[0],"old name":data[1],"male":int(data[2]),"female":int(data[3]),"english":int(data[4]),"hindi":int(data[5]),"punjabi":int(data[6]),"bangoli":int(data[7]),"noise":int(data[8]),"check":int(data[9])}

    return ans


def getdata(index:int) ->dict:
    #print(data)
    return list2dict(data[index])





