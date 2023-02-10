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


for member in MEMBERS:

    try:
        createFolder("./merged")
    
        targetFATH = "./tasking/*/" + member + ".csv"
        saveFATH = "./merged/" + member + ".csv"

        # csv 리스트 받아오기
        csv_list = glob.glob(targetFATH)

        # 파일 Union 선언
        df = pd.DataFrame()
        for f in range(0, len(csv_list)):  # 예를들어 202301, 202302 로 된 파일이면 2023_*
            temp_df = pd.read_csv(csv_list[f])
            df = df.append(temp_df, ignore_index=True)

        # 데이터갯수확인
        # print(df.shape)
        # 데이터 잘 들어오는지 확인
        # print(df)

        # 결측치 변경
        df.replace(-1, 0, inplace=True)

        # 날짜 자릿수 변경
        df = df.astype({"date":"int"})
        df.loc[(df["date"] < 999) & (df["date"] > 800),
               "date"] = 20220000 + df["date"]
        df.loc[(df["date"] > 999) & (df["date"] < 1300),
               "date"] = 20220000 + df["date"]
        df.loc[df["date"] < 800, "date"] = 20230000 + df["date"]

        # 컬럼 변경
        df["user_id"] = "S" + member
        df = df[["date", "user_id", "All", "mAcc", "mGyr",
                 "mPre", "mLi", "wAcc", "wGyr", "wPre", "wHR"]]
        df = df.rename(columns={"All": "minimum_per"})

        # 파일저장
        df.to_csv(path_or_buf=saveFATH,
                  sep=",",
                  na_rep="0",
                  float_format="%.2f",  # 2 decimal places
                  index=False)  # do not write index

    except Exception as e:
        print("[ERROR]\t"+member, e)
        pass

    print("[Done]\t" + member)

print("[Mission Complete]")

all_merge_saveFATH = "./all_merged/all.csv"
all_merge_targetFATH = "./merged/*.csv"
all_merge_csv_list = glob.glob(all_merge_targetFATH)

# 파일 Union 선언
df = pd.DataFrame()
for f in range(0, len(all_merge_csv_list)):
    temp_df = pd.read_csv(all_merge_csv_list[f])
    df = df.append(temp_df, ignore_index=True)

# 파일저장
df.to_csv(path_or_buf=all_merge_saveFATH,
            sep=",",
            na_rep="0",
            float_format="%.2f",  # 2 decimal places
            index=False)  # do not write index
