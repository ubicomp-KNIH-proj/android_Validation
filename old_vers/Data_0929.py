# Created by C. Msigwa, SCH Univ.,

import requests
import numpy as np
import datetime

class ServerData:

    # init method or constructor
    def __init__(self, Ae_Name, Ae_Sensor, Ae_device, Start_Day, Start_Month):
        self.Ae_Name = Ae_Name
        self.Ae_Sensor = Ae_Sensor
        self.Ae_device = Ae_device

        self.Start_Day = int(Start_Day)
        self.Start_Month = int(Start_Month)
        # self.Loop_Count = int(Loop_Count)

        self.Start_Date = datetime.datetime(2022, self.Start_Month, self.Start_Day)
        self.End_Date = self.Start_Date + datetime.timedelta(days=1)

        self.cra = '&cra=2022' + self.Start_Date.strftime("%m%d") + 'T000000'
        self.crb = '&crb=2022' + self.End_Date.strftime("%m%d") + 'T000000'

    # Sample Method
    def Send_Data(self):

        url = "http://114.71.220.59:7579/Mobius/S" + self.Ae_Name + "/" + self.Ae_device + "/" + self.Ae_Sensor + "?fu=2&ty=4&rcn=4" + self.cra + self.crb
        # url = "http://114.71.220.59:7579/Mobius/S" + self.Ae_Name + "/" + self.Ae_device + "/" + self.Ae_Sensor + "?fu=2&ty=4&rcn=4" + '&cra=20220901T000000&crb=20220902T000000'
        headers = {'Accept': 'application/json', 'X-M2M-RI': '12345', 'X-M2M-Origin': 'SOrigin'}

        Listdata = []

        r = requests.get(url, headers=headers)
        print(r.status_code)
        if (r.status_code == 200):
            try:
                r.raise_for_status()
                jr = r.json()
                lst = jr['m2m:rsp']['m2m:cin']
                for i in lst:
                    CurrentData = i['con'].split(',')
                    if CurrentData[0] != "None":
                        Listdata.append(list(np.float_(CurrentData)))

                Flat_Data = [item for sublist in Listdata for item in sublist]

                #print(Flat_Data)
                return Flat_Data
            except Exception as exc:
                print('There was a problem: %s' % (exc))
        else:
            print("FAILED NEGATIVE RESPONSE")
            return [0]

    def Evaluate_Data(self):
        print("ok")
