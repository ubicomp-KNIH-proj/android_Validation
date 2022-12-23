import pandas as pd
from glob import glob

# MEMBER = "S604"
# FILE_PATH = "KNIH_Total_Data/" + MEMBER

# MEMBERS = ["604","605"]

# 12월 22일 기준 실험 종료 유저
MEMBERS3 = ["604","605","609","610","611","612","613","615","616","618","620","621","624","625","628","629","631","632","633","634","636","641","643","650","651","652","653"]
date3 = "_20221014_20221222"

# 11월 17일 기준 실험 종료 유저
MEMBERS2 = ["607", "608", "622", "630"]
date2 = "_20220919_20221117"

# 11월 16일 기준 실험 종료 유저
MEMBERS1 = ["619"]
date1 = "_20220918_20221116"

# 11월 12일 기준 실험 종료 유저
MEMBERS = ["603"]
date = "_20220914_20221112"

# # 10월 24일 기준 실험 종료 유저
# MEMBERS = ["606","614"]
# date = "_20220826_20221024"


for member in MEMBERS:
    print(f"user : {member}") # 확인용
    FILE_PATH = "D:/KNIH병합하기병합하기/KNIH_Total_Data/S" + member + "/S" + member # 파일 쓸 경로 설정

    ### mAcc ###
    file_names_1 = glob("D:/KNIH병합하기병합하기/KNIH_MERGE_FOLD/S" + member + "/*mAcc.csv")
    total_1 = pd.DataFrame()
    print(file_names_1)

    for file_name_1 in file_names_1:
        try:
            temp_1 = pd.read_csv(file_name_1, sep=',',header= None, on_bad_lines='skip', encoding='utf-8') 
        except pd.errors.EmptyDataError:
            continue

        total_1 = pd.concat([total_1, temp_1]) 
        print(f"{file_name_1} is Done.")

    total_1.to_csv(FILE_PATH + "_mAcc" + date + ".csv")
    print("mAcc Done!!")


    ### mGyr ###
    file_names_2 = glob("D:/KNIH병합하기병합하기/KNIH_MERGE_FOLD/S" + member + "/*mGyr.csv")
    total_2 = pd.DataFrame()
    print(file_names_2)
   
    for file_name_2 in file_names_2:
        try:
            temp_2 = pd.read_csv(file_name_2, sep=',',header= None, on_bad_lines='skip', encoding='utf-8') 
        except pd.errors.EmptyDataError:
            continue

        total_2 = pd.concat([total_2, temp_2]) 
        print(f"{file_name_2} is Done.")

    total_2.to_csv(FILE_PATH + "_mGyr" + date + ".csv")
    print("mGyr Done!!")


    ### mLi ###
    file_names_3 = glob("D:/KNIH병합하기병합하기/KNIH_MERGE_FOLD/S" + member + "/*mLi.csv")
    total_3 = pd.DataFrame()
    print(file_names_3)

    for file_name_3 in file_names_3:
        try:
            temp_3 = pd.read_csv(file_name_3, sep=',',header= None, on_bad_lines='skip', encoding='utf-8') 
        except pd.errors.EmptyDataError:
            continue

        total_3 = pd.concat([total_3, temp_3]) 
        print(f"{file_name_3} is Done.")

    total_3.to_csv(FILE_PATH + "_mLi" + date + ".csv")
    print("mLi Done!!")


    ### mPre ###
    file_names_4 = glob("D:/KNIH병합하기병합하기/KNIH_MERGE_FOLD/S" + member + "/*mPre.csv")
    total_4 = pd.DataFrame()
    print(file_names_4)
    
    for file_name_4 in file_names_4:
        try:
            temp_4 = pd.read_csv(file_name_4, sep=',',header= None, on_bad_lines='skip', encoding='utf-8') 
        except pd.errors.EmptyDataError:
            continue

        total_4 = pd.concat([total_4, temp_4]) 
        print(f"{file_name_4} is Done.")

    total_4.to_csv(FILE_PATH + "_mPre" + date + ".csv")
    print("mPre Done!!")


    ### wAcc ###
    file_names_5 = glob("D:/KNIH병합하기병합하기/KNIH_MERGE_FOLD/S" + member + "/*wAcc.csv")
    total_5 = pd.DataFrame()
    print(file_names_5)
    
    for file_name_5 in file_names_5:
        try:
            temp_5 = pd.read_csv(file_name_5, sep=',',header= None, on_bad_lines='skip', encoding='utf-8') 
        except pd.errors.EmptyDataError:
            continue
            
        total_5 = pd.concat([total_5, temp_5]) 
        print(f"{file_name_5} is Done.")

    total_5.to_csv(FILE_PATH + "_wAcc" + date + ".csv")
    print("wAcc Done!!")


    ### wGyr ###
    file_names_6 = glob("D:/KNIH병합하기병합하기/KNIH_MERGE_FOLD/S" + member + "/*wGyr.csv")
    total_6 = pd.DataFrame()
    print(file_names_6)

    for file_name_6 in file_names_6:
        try:
            temp_6 = pd.read_csv(file_name_6, sep=',',header= None, on_bad_lines='skip', encoding='utf-8') 
        except pd.errors.EmptyDataError:
            continue

        total_6 = pd.concat([total_6, temp_6]) 
        print(f"{file_name_6} is Done.")

    total_6.to_csv(FILE_PATH + "_wGyr" + date + ".csv")
    print("wGyr Done!!")


    ### wHR ###
    file_names_7 = glob("D:/KNIH병합하기병합하기/KNIH_MERGE_FOLD/S" + member + "/*wHR.csv")
    total_7 = pd.DataFrame()
    print(file_names_7)

    for file_name_7 in file_names_7:
        try:
            temp_7 = pd.read_csv(file_name_7, sep=',',header= None, on_bad_lines='skip', encoding='utf-8') 
        except pd.errors.EmptyDataError:
            continue

        total_7 = pd.concat([total_7, temp_7]) 
        print(f"{file_name_7} is Done.")

    total_7.to_csv(FILE_PATH + "_wHR" + date + ".csv")
    print("wHR Done!!")


    ### wPre ###
    file_names_8 = glob("D:/KNIH병합하기병합하기/KNIH_MERGE_FOLD/S" + member + "/*wPre.csv")
    total_8 = pd.DataFrame()
    print(file_names_8)

    for file_name_8 in file_names_8:
        try:
            temp_8 = pd.read_csv(file_name_8, sep=',',header= None, on_bad_lines='skip', encoding='utf-8') 
        except pd.errors.EmptyDataError:
            continue

        total_8 = pd.concat([total_8, temp_8]) 
        print(f"{file_name_8} is Done.")

    total_8.to_csv(FILE_PATH + "wPre" + date + ".csv")
    print("wPre Done!!")

    print(f"{member} Done")


for member in MEMBERS1:
    print(f"user : {member}") # 확인용
    FILE_PATH = "D:/KNIH병합하기병합하기/KNIH_Total_Data/S" + member + "/S" + member # 파일 쓸 경로 설정

    ### mAcc ###
    file_names_1 = glob("D:/KNIH병합하기병합하기/KNIH_MERGE_FOLD/S" + member + "/*mAcc.csv")
    total_1 = pd.DataFrame()
    print(file_names_1)

    for file_name_1 in file_names_1:
        try:
            temp_1 = pd.read_csv(file_name_1, sep=',',header= None, on_bad_lines='skip', encoding='utf-8') 
        except pd.errors.EmptyDataError:
            continue

        total_1 = pd.concat([total_1, temp_1]) 
        print(f"{file_name_1} is Done.")

    total_1.to_csv(FILE_PATH + "_mAcc" + date1 + ".csv")
    print("mAcc Done!!")


    ### mGyr ###
    file_names_2 = glob("D:/KNIH병합하기병합하기/KNIH_MERGE_FOLD/S" + member + "/*mGyr.csv")
    total_2 = pd.DataFrame()
    print(file_names_2)
   
    for file_name_2 in file_names_2:
        try:
            temp_2 = pd.read_csv(file_name_2, sep=',',header= None, on_bad_lines='skip', encoding='utf-8') 
        except pd.errors.EmptyDataError:
            continue

        total_2 = pd.concat([total_2, temp_2]) 
        print(f"{file_name_2} is Done.")

    total_2.to_csv(FILE_PATH + "_mGyr" + date1 + ".csv")
    print("mGyr Done!!")


    ### mLi ###
    file_names_3 = glob("D:/KNIH병합하기병합하기/KNIH_MERGE_FOLD/S" + member + "/*mLi.csv")
    total_3 = pd.DataFrame()
    print(file_names_3)

    for file_name_3 in file_names_3:
        try:
            temp_3 = pd.read_csv(file_name_3, sep=',',header= None, on_bad_lines='skip', encoding='utf-8') 
        except pd.errors.EmptyDataError:
            continue

        total_3 = pd.concat([total_3, temp_3]) 
        print(f"{file_name_3} is Done.")

    total_3.to_csv(FILE_PATH + "_mLi" + date1 + ".csv")
    print("mLi Done!!")


    ### mPre ###
    file_names_4 = glob("D:/KNIH병합하기병합하기/KNIH_MERGE_FOLD/S" + member + "/*mPre.csv")
    total_4 = pd.DataFrame()
    print(file_names_4)
    
    for file_name_4 in file_names_4:
        try:
            temp_4 = pd.read_csv(file_name_4, sep=',',header= None, on_bad_lines='skip', encoding='utf-8') 
        except pd.errors.EmptyDataError:
            continue

        total_4 = pd.concat([total_4, temp_4]) 
        print(f"{file_name_4} is Done.")

    total_4.to_csv(FILE_PATH + "_mPre" + date1 + ".csv")
    print("mPre Done!!")


    ### wAcc ###
    file_names_5 = glob("D:/KNIH병합하기병합하기/KNIH_MERGE_FOLD/S" + member + "/*wAcc.csv")
    total_5 = pd.DataFrame()
    print(file_names_5)
    
    for file_name_5 in file_names_5:
        try:
            temp_5 = pd.read_csv(file_name_5, sep=',',header= None, on_bad_lines='skip', encoding='utf-8') 
        except pd.errors.EmptyDataError:
            continue
            
        total_5 = pd.concat([total_5, temp_5]) 
        print(f"{file_name_5} is Done.")

    total_5.to_csv(FILE_PATH + "_wAcc" + date1 + ".csv")
    print("wAcc Done!!")


    ### wGyr ###
    file_names_6 = glob("D:/KNIH병합하기병합하기/KNIH_MERGE_FOLD/S" + member + "/*wGyr.csv")
    total_6 = pd.DataFrame()
    print(file_names_6)

    for file_name_6 in file_names_6:
        try:
            temp_6 = pd.read_csv(file_name_6, sep=',',header= None, on_bad_lines='skip', encoding='utf-8') 
        except pd.errors.EmptyDataError:
            continue

        total_6 = pd.concat([total_6, temp_6]) 
        print(f"{file_name_6} is Done.")

    total_6.to_csv(FILE_PATH + "_wGyr" + date1 + ".csv")
    print("wGyr Done!!")


    ### wHR ###
    file_names_7 = glob("D:/KNIH병합하기병합하기/KNIH_MERGE_FOLD/S" + member + "/*wHR.csv")
    total_7 = pd.DataFrame()
    print(file_names_7)

    for file_name_7 in file_names_7:
        try:
            temp_7 = pd.read_csv(file_name_7, sep=',',header= None, on_bad_lines='skip', encoding='utf-8') 
        except pd.errors.EmptyDataError:
            continue

        total_7 = pd.concat([total_7, temp_7]) 
        print(f"{file_name_7} is Done.")

    total_7.to_csv(FILE_PATH + "_wHR" + date1 + ".csv")
    print("wHR Done!!")


    ### wPre ###
    file_names_8 = glob("D:/KNIH병합하기병합하기/KNIH_MERGE_FOLD/S" + member + "/*wPre.csv")
    total_8 = pd.DataFrame()
    print(file_names_8)

    for file_name_8 in file_names_8:
        try:
            temp_8 = pd.read_csv(file_name_8, sep=',',header= None, on_bad_lines='skip', encoding='utf-8') 
        except pd.errors.EmptyDataError:
            continue

        total_8 = pd.concat([total_8, temp_8]) 
        print(f"{file_name_8} is Done.")

    total_8.to_csv(FILE_PATH + "wPre" + date1 + ".csv")
    print("wPre Done!!")

    print(f"{member} Done")


for member in MEMBERS2:
    print(f"user : {member}") # 확인용
    FILE_PATH = "D:/KNIH병합하기병합하기/KNIH_Total_Data/S" + member + "/S" + member # 파일 쓸 경로 설정

    ### mAcc ###
    file_names_1 = glob("D:/KNIH병합하기병합하기/KNIH_MERGE_FOLD/S" + member + "/*mAcc.csv")
    total_1 = pd.DataFrame()
    print(file_names_1)

    for file_name_1 in file_names_1:
        try:
            temp_1 = pd.read_csv(file_name_1, sep=',',header= None, on_bad_lines='skip', encoding='utf-8') 
        except pd.errors.EmptyDataError:
            continue

        total_1 = pd.concat([total_1, temp_1]) 
        print(f"{file_name_1} is Done.")

    total_1.to_csv(FILE_PATH + "_mAcc" + date2 + ".csv")
    print("mAcc Done!!")


    ### mGyr ###
    file_names_2 = glob("D:/KNIH병합하기병합하기/KNIH_MERGE_FOLD/S" + member + "/*mGyr.csv")
    total_2 = pd.DataFrame()
    print(file_names_2)
   
    for file_name_2 in file_names_2:
        try:
            temp_2 = pd.read_csv(file_name_2, sep=',',header= None, on_bad_lines='skip', encoding='utf-8') 
        except pd.errors.EmptyDataError:
            continue

        total_2 = pd.concat([total_2, temp_2]) 
        print(f"{file_name_2} is Done.")

    total_2.to_csv(FILE_PATH + "_mGyr" + date2 + ".csv")
    print("mGyr Done!!")


    ### mLi ###
    file_names_3 = glob("D:/KNIH병합하기병합하기/KNIH_MERGE_FOLD/S" + member + "/*mLi.csv")
    total_3 = pd.DataFrame()
    print(file_names_3)

    for file_name_3 in file_names_3:
        try:
            temp_3 = pd.read_csv(file_name_3, sep=',',header= None, on_bad_lines='skip', encoding='utf-8') 
        except pd.errors.EmptyDataError:
            continue

        total_3 = pd.concat([total_3, temp_3]) 
        print(f"{file_name_3} is Done.")

    total_3.to_csv(FILE_PATH + "_mLi" + date2 + ".csv")
    print("mLi Done!!")


    ### mPre ###
    file_names_4 = glob("D:/KNIH병합하기병합하기/KNIH_MERGE_FOLD/S" + member + "/*mPre.csv")
    total_4 = pd.DataFrame()
    print(file_names_4)
    
    for file_name_4 in file_names_4:
        try:
            temp_4 = pd.read_csv(file_name_4, sep=',',header= None, on_bad_lines='skip', encoding='utf-8') 
        except pd.errors.EmptyDataError:
            continue

        total_4 = pd.concat([total_4, temp_4]) 
        print(f"{file_name_4} is Done.")

    total_4.to_csv(FILE_PATH + "_mPre" + date2 + ".csv")
    print("mPre Done!!")


    ### wAcc ###
    file_names_5 = glob("D:/KNIH병합하기병합하기/KNIH_MERGE_FOLD/S" + member + "/*wAcc.csv")
    total_5 = pd.DataFrame()
    print(file_names_5)
    
    for file_name_5 in file_names_5:
        try:
            temp_5 = pd.read_csv(file_name_5, sep=',',header= None, on_bad_lines='skip', encoding='utf-8') 
        except pd.errors.EmptyDataError:
            continue
            
        total_5 = pd.concat([total_5, temp_5]) 
        print(f"{file_name_5} is Done.")

    total_5.to_csv(FILE_PATH + "_wAcc" + date2 + ".csv")
    print("wAcc Done!!")


    ### wGyr ###
    file_names_6 = glob("D:/KNIH병합하기병합하기/KNIH_MERGE_FOLD/S" + member + "/*wGyr.csv")
    total_6 = pd.DataFrame()
    print(file_names_6)

    for file_name_6 in file_names_6:
        try:
            temp_6 = pd.read_csv(file_name_6, sep=',',header= None, on_bad_lines='skip', encoding='utf-8') 
        except pd.errors.EmptyDataError:
            continue

        total_6 = pd.concat([total_6, temp_6]) 
        print(f"{file_name_6} is Done.")

    total_6.to_csv(FILE_PATH + "_wGyr" + date2 + ".csv")
    print("wGyr Done!!")


    ### wHR ###
    file_names_7 = glob("D:/KNIH병합하기병합하기/KNIH_MERGE_FOLD/S" + member + "/*wHR.csv")
    total_7 = pd.DataFrame()
    print(file_names_7)

    for file_name_7 in file_names_7:
        try:
            temp_7 = pd.read_csv(file_name_7, sep=',',header= None, on_bad_lines='skip', encoding='utf-8') 
        except pd.errors.EmptyDataError:
            continue

        total_7 = pd.concat([total_7, temp_7]) 
        print(f"{file_name_7} is Done.")

    total_7.to_csv(FILE_PATH + "_wHR" + date2 + ".csv")
    print("wHR Done!!")


    ### wPre ###
    file_names_8 = glob("D:/KNIH병합하기병합하기/KNIH_MERGE_FOLD/S" + member + "/*wPre.csv")
    total_8 = pd.DataFrame()
    print(file_names_8)

    for file_name_8 in file_names_8:
        try:
            temp_8 = pd.read_csv(file_name_8, sep=',',header= None, on_bad_lines='skip', encoding='utf-8') 
        except pd.errors.EmptyDataError:
            continue

        total_8 = pd.concat([total_8, temp_8]) 
        print(f"{file_name_8} is Done.")

    total_8.to_csv(FILE_PATH + "wPre" + date2 + ".csv")
    print("wPre Done!!")

    print(f"{member} Done")


for member in MEMBERS3:
    print(f"user : {member}") # 확인용
    FILE_PATH = "D:/KNIH병합하기병합하기/KNIH_Total_Data/S" + member + "/S" + member # 파일 쓸 경로 설정

    ### mAcc ###
    file_names_1 = glob("D:/KNIH병합하기병합하기/KNIH_MERGE_FOLD/S" + member + "/*mAcc.csv")
    total_1 = pd.DataFrame()
    print(file_names_1)

    for file_name_1 in file_names_1:
        try:
            temp_1 = pd.read_csv(file_name_1, sep=',',header= None, on_bad_lines='skip', encoding='utf-8') 
        except pd.errors.EmptyDataError:
            continue

        total_1 = pd.concat([total_1, temp_1]) 
        print(f"{file_name_1} is Done.")

    total_1.to_csv(FILE_PATH + "_mAcc" + date3 + ".csv")
    print("mAcc Done!!")


    ### mGyr ###
    file_names_2 = glob("D:/KNIH병합하기병합하기/KNIH_MERGE_FOLD/S" + member + "/*mGyr.csv")
    total_2 = pd.DataFrame()
    print(file_names_2)
   
    for file_name_2 in file_names_2:
        try:
            temp_2 = pd.read_csv(file_name_2, sep=',',header= None, on_bad_lines='skip', encoding='utf-8') 
        except pd.errors.EmptyDataError:
            continue

        total_2 = pd.concat([total_2, temp_2]) 
        print(f"{file_name_2} is Done.")

    total_2.to_csv(FILE_PATH + "_mGyr" + date3 + ".csv")
    print("mGyr Done!!")


    ### mLi ###
    file_names_3 = glob("D:/KNIH병합하기병합하기/KNIH_MERGE_FOLD/S" + member + "/*mLi.csv")
    total_3 = pd.DataFrame()
    print(file_names_3)

    for file_name_3 in file_names_3:
        try:
            temp_3 = pd.read_csv(file_name_3, sep=',',header= None, on_bad_lines='skip', encoding='utf-8') 
        except pd.errors.EmptyDataError:
            continue

        total_3 = pd.concat([total_3, temp_3]) 
        print(f"{file_name_3} is Done.")

    total_3.to_csv(FILE_PATH + "_mLi" + date3 + ".csv")
    print("mLi Done!!")


    ### mPre ###
    file_names_4 = glob("D:/KNIH병합하기병합하기/KNIH_MERGE_FOLD/S" + member + "/*mPre.csv")
    total_4 = pd.DataFrame()
    print(file_names_4)
    
    for file_name_4 in file_names_4:
        try:
            temp_4 = pd.read_csv(file_name_4, sep=',',header= None, on_bad_lines='skip', encoding='utf-8') 
        except pd.errors.EmptyDataError:
            continue

        total_4 = pd.concat([total_4, temp_4]) 
        print(f"{file_name_4} is Done.")

    total_4.to_csv(FILE_PATH + "_mPre" + date3 + ".csv")
    print("mPre Done!!")


    ### wAcc ###
    file_names_5 = glob("D:/KNIH병합하기병합하기/KNIH_MERGE_FOLD/S" + member + "/*wAcc.csv")
    total_5 = pd.DataFrame()
    print(file_names_5)
    
    for file_name_5 in file_names_5:
        try:
            temp_5 = pd.read_csv(file_name_5, sep=',',header= None, on_bad_lines='skip', encoding='utf-8') 
        except pd.errors.EmptyDataError:
            continue
            
        total_5 = pd.concat([total_5, temp_5]) 
        print(f"{file_name_5} is Done.")

    total_5.to_csv(FILE_PATH + "_wAcc" + date3 + ".csv")
    print("wAcc Done!!")


    ### wGyr ###
    file_names_6 = glob("D:/KNIH병합하기병합하기/KNIH_MERGE_FOLD/S" + member + "/*wGyr.csv")
    total_6 = pd.DataFrame()
    print(file_names_6)

    for file_name_6 in file_names_6:
        try:
            temp_6 = pd.read_csv(file_name_6, sep=',',header= None, on_bad_lines='skip', encoding='utf-8') 
        except pd.errors.EmptyDataError:
            continue

        total_6 = pd.concat([total_6, temp_6]) 
        print(f"{file_name_6} is Done.")

    total_6.to_csv(FILE_PATH + "_wGyr" + date3 + ".csv")
    print("wGyr Done!!")


    ### wHR ###
    file_names_7 = glob("D:/KNIH병합하기병합하기/KNIH_MERGE_FOLD/S" + member + "/*wHR.csv")
    total_7 = pd.DataFrame()
    print(file_names_7)

    for file_name_7 in file_names_7:
        try:
            temp_7 = pd.read_csv(file_name_7, sep=',',header= None, on_bad_lines='skip', encoding='utf-8') 
        except pd.errors.EmptyDataError:
            continue

        total_7 = pd.concat([total_7, temp_7]) 
        print(f"{file_name_7} is Done.")

    total_7.to_csv(FILE_PATH + "_wHR" + date3 + ".csv")
    print("wHR Done!!")


    ### wPre ###
    file_names_8 = glob("D:/KNIH병합하기병합하기/KNIH_MERGE_FOLD/S" + member + "/*wPre.csv")
    total_8 = pd.DataFrame()
    print(file_names_8)

    for file_name_8 in file_names_8:
        try:
            temp_8 = pd.read_csv(file_name_8, sep=',',header= None, on_bad_lines='skip', encoding='utf-8') 
        except pd.errors.EmptyDataError:
            continue

        total_8 = pd.concat([total_8, temp_8]) 
        print(f"{file_name_8} is Done.")

    total_8.to_csv(FILE_PATH + "wPre" + date3 + ".csv")
    print("wPre Done!!")

    print(f"{member} Done")



print(" ")
print("!!! ALL DONE !!!")

