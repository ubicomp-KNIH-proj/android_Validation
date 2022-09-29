# Created by C. Msigwa, SCH Univ.,
from datetime import datetime
import csv
from Data_0929 import ServerData
import os

# A Sample class with init method
class Write_Csv(object):
    def __init__(self, ReceivedData):
        self.ReceivedData = ReceivedData

    def CSV_FILE(self,Ae_Name,Ae_Sensor, Start_Day, Start_Month):
        
        if len(Start_Month) == 1:
            Start_Month = "0" + Start_Month

        dt_string = Start_Month + Start_Day
        physio_id = Ae_Sensor

        csv_Folder_Root = "S" + Ae_Name
        val_Folder_Root = "val/S" + Ae_Name
        csv_Root = "./S" + Ae_Name +"/" + Ae_Name +  "_"  + dt_string + "_" + physio_id + ".csv"

        try:
            if not os.path.exists(csv_Folder_Root):
                os.makedirs(csv_Folder_Root)
        except OSError:
            print('Error: Creating directory. ' + csv_Folder_Root)
            
        try:
            if not os.path.exists(val_Folder_Root):
                os.makedirs(val_Folder_Root)
        except OSError:
            print('Error: Creating directory. ' + val_Folder_Root)


        with open(csv_Root, 'a', encoding='UTF8') as f:
            for i in self.ReceivedData:
                    ##One second data that you can write to csv is available here
                    writer = csv.writer(f, lineterminator='\n')
                    writer.writerow(i)
                    #print(i)

class Mobius_Data(Write_Csv):
    # init method or constructor
    def __init__(self, data):
        self.data = data

    # Sample Method
    def Processing_Data(self):
        ts = 1643.0
        DateInformation = []
        for i in range(100):
            new = ts + 1
            ts = new
            DateInformation.append(new)
        Lastindex = len(self.data) - 1
        amount = 0

        for j in DateInformation:
            amount = amount + self.data.count(j)

        indexes = []
        subList = []

        for i in range(0, len(self.data), 1):
            if self.data[i] in DateInformation: 
                indexes.append(i)

        for j in range(amount):
            if len(indexes) > 1:
                subList.append(self.data[indexes[0]:indexes[1]])
                del indexes[:1]
        
            else:
                subList.append(self.data[indexes[0]:Lastindex])
                del indexes[:1]

        # Calling init of parent class
        Write_Csv.__init__(self, subList)

def main(Ae_Name, Ae_Sensor, Ae_device, Start_Day, Start_Month):
    data = ServerData(Ae_Name, Ae_Sensor, Ae_device, Start_Day, Start_Month)
    p = Mobius_Data(data.Send_Data())

    
    p.Processing_Data()
    p.CSV_FILE(Ae_Name,Ae_Sensor, Start_Day, Start_Month)

if __name__ == "__main__":
    devices = ["mobile","watch"]
    sensors = ["mAcc","mPre","mLi","mGyr","wHR","wPre","wAcc","wGyr"]
    Ae_Name = input('Input [AE], EX) S618 => 618\n')  # User ID

    Start_Month = input('Input [Month], EX) 9월 => 9\n')
    Start_Day = input('Input [Month], EX) 10일 => 10\n')
    # Loop_Count = input('Input Loop')

    for device in devices:
        Ae_device = device #watch,mobile

        for sensor in sensors:
            Ae_Sensor = sensor   ##M mAcc,mPre,mLight,mGyro,wHR,wPre,wAcc,wGyr
            main(Ae_Name, Ae_Sensor, Ae_device, Start_Day, Start_Month)
        
            print("Done\t" + sensor)

    print("ALL DONE")