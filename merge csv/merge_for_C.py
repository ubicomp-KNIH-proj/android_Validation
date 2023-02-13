import pandas as pd
import glob
import os

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("Error: Creating directory. " + directory)


MEMBERS = ["601", "602", "603", "604", "605", "606", "607", "608", "609", "610",
           "611", "612", "613", "614", "615", "616", "617", "618", "619", "620",
           "621", "622", "623", "624", "625", "627", "628", "629", "630", "631",
           "632", "633", "634", "635", "636", "637", "638", "639", "641", "643",
           "644", "645", "650", "651", "652", "653", "660", "661", "663", "664",
           "665"]

createFolder("./merged")


for member in MEMBERS:

    try:

        targetFATH = "./tasking/" + member + ".csv"
        saveFATH = "./merged/" + member + ".csv"

        # 파일 Union 선언
        df = pd.DataFrame()
        temp_df = pd.read_csv(targetFATH)
        df = df.append(temp_df, ignore_index=True)

        # 중복 제거
        df = df.drop_duplicates(['date'], keep = 'first')

        # 파일저장
        df.to_csv(path_or_buf=saveFATH,
                    sep=",",
                    na_rep="0",
                    float_format="%.2f",  # 2 decimal places
                    index=False)  # do not write index
        
    except Exception as e:
        print(member, e)
        pass
