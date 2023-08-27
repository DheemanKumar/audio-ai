import csv

# CSV file path
language="hindi"
csv_file =language+"_unprocessed_audio_data.csv"
header=[]

# Read data from CSV file
data = []
with open(csv_file, mode="r") as file:
    reader = csv.reader(file)
    header = next(reader)  # Read the header row
    for row in reader:
        data.append(row)



def savedata(Data=data, Header=header, csv_file="unprocessed_audio_data.csv"):
    with open(csv_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(Header)  # Write the header row
        writer.writerows(Data)    # Write the updated data


def updatedata(index:int,given_data:dict):
    data[index][1]=int(given_data["male"])
    data[index][2]=int(given_data["female"])
    data[index][3]=int(given_data["english"])
    data[index][4]=int(given_data["hindi"])
    data[index][5]=int(given_data["punjabi"])
    data[index][6]=int(given_data["bangoli"])
    data[index][7]=int(given_data["noise"])


def dict2list():
    pass

def list2dict(data:list) ->dict:
    if len(data)!=8:
        return FileNotFoundError
    ans={"name":data[0],"male":int(data[1]),"female":int(data[2]),"english":int(data[3]),"hindi":int(data[4]),"punjabi":int(data[5]),"bangoli":int(data[6]),"noise":int(data[7])}

    return ans


def getdata(index:int) ->dict:
    return list2dict(data[index])





