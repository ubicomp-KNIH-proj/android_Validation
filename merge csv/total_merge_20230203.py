import pandas as pd
from glob import glob

# MEMBER = "S604"
# FILE_PATH = "KNIH_Total_Data/" + MEMBER

# MEMBERS = ["604","605"]


MEMBERS = ['601','602','603','604','605','606','607','608','609','610','611','612','613','614','615','616','617','618','619','620','621','622','623','624','625','627','628','629','630','631','632','633','634','635','636','637','638','639','641','643','644','645','650','651','652','653']
date = "_2022_2022"

col_Load_List_mAcc = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34']
col_Load_List_mGyr = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34']
col_Load_List_mLi = ['0','1','2','3']
col_Load_List_mPre = ['0','1','2','3']

col_Load_List_wAcc = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34']
col_Load_List_wGyr = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34']
col_Load_List_wHR = ['0','1','2','3']
col_Load_List_wPre = ['0','1','2','3']



for member in MEMBERS:
    print(f"user : {member}") # 확인용
    FILE_PATH = "D:/KNIH병합하기병합하기나스에올리기/KNIH_Total_Data/" + member + "/S" + member # 파일 쓸 경로 설정

    ### mAcc ###
    file_names_1 = glob("D:/KNIH병합하기병합하기나스에올리기/KNIH_MERGE_FOLD/S" + member + "/*mAcc.csv")
    total_1 = pd.DataFrame()
    print(file_names_1)

    for file_name_1 in file_names_1:
        try:
            temp_1 = pd.read_csv(file_name_1, sep=',',header= None, names= col_Load_List_mAcc, encoding='utf-8') 
        except:
            temp_1 = pd.read_csv(file_name_1, sep=',',header= None, on_bad_lines='warn', encoding='utf-8') 
            continue
        
        total_1 = pd.concat([total_1, temp_1]) 
        print(f"{file_name_1} is Done.")

    print("Let's GO!")
    total_1.to_csv(FILE_PATH + "_mAcc" + date + ".csv", encoding= 'utf-8', index= False)
    print("mAcc Done!!")


    ### mGyr ###
    file_names_2 = glob("D:/KNIH병합하기병합하기나스에올리기/KNIH_MERGE_FOLD/S" + member + "/*mGyr.csv")
    total_2 = pd.DataFrame()
    print(file_names_2)
   
    for file_name_2 in file_names_2:
        try:
            temp_2 = pd.read_csv(file_name_2, sep=',',header= None, names= col_Load_List_mGyr, encoding='utf-8') 
        except:
            temp_2 = pd.read_csv(file_name_2, sep=',',header= None, on_bad_lines='warn', encoding='utf-8') 
            continue

        total_2 = pd.concat([total_2, temp_2]) 
        print(f"{file_name_2} is Done.")

    print("Let's GO!")
    total_2.to_csv(FILE_PATH + "_mGyr" + date + ".csv", encoding= 'utf-8', index= False)
    print("mGyr Done!!")


    ### mLi ###
    file_names_3 = glob("D:/KNIH병합하기병합하기나스에올리기/KNIH_MERGE_FOLD/S" + member + "/*mLi.csv")
    total_3 = pd.DataFrame()
    print(file_names_3)

    for file_name_3 in file_names_3:
        try:
            temp_3 = pd.read_csv(file_name_3, sep=',',header= None, names= col_Load_List_mLi, encoding='utf-8') 
        except:
            temp_3 = pd.read_csv(file_name_3, sep=',',header= None, on_bad_lines='warn', encoding='utf-8') 
            continue

        total_3 = pd.concat([total_3, temp_3]) 
        print(f"{file_name_3} is Done.")

    print("Let's GO!")
    total_3.to_csv(FILE_PATH + "_mLi" + date + ".csv", encoding= 'utf-8', index= False)
    print("mLi Done!!")


    ### mPre ###
    file_names_4 = glob("D:/KNIH병합하기병합하기나스에올리기/KNIH_MERGE_FOLD/S" + member + "/*mPre.csv")
    total_4 = pd.DataFrame()
    print(file_names_4)
    
    for file_name_4 in file_names_4:
        try:
            temp_4 = pd.read_csv(file_name_4, sep=',',header= None, names= col_Load_List_mPre, encoding='utf-8') 
        except:
            temp_4 = pd.read_csv(file_name_4, sep=',',header= None, on_bad_lines='warn', encoding='utf-8') 
            continue

        total_4 = pd.concat([total_4, temp_4]) 
        print(f"{file_name_4} is Done.")

    print("Let's GO!")
    total_4.to_csv(FILE_PATH + "_mPre" + date + ".csv", encoding= 'utf-8', index= False)
    print("mPre Done!!")


    ### wAcc ###
    file_names_5 = glob("D:/KNIH병합하기병합하기나스에올리기/KNIH_MERGE_FOLD/S" + member + "/*wAcc.csv")
    total_5 = pd.DataFrame()
    print(file_names_5)
    
    for file_name_5 in file_names_5:
        try:
            temp_5 = pd.read_csv(file_name_5, sep=',',header= None, names= col_Load_List_wAcc, encoding='utf-8') 
        except:
            temp_5 = pd.read_csv(file_name_5, sep=',',header= None, on_bad_lines='warn', encoding='utf-8') 
            continue
            
        total_5 = pd.concat([total_5, temp_5]) 
        print(f"{file_name_5} is Done.")

    print("Let's GO!")
    total_5.to_csv(FILE_PATH + "_wAcc" + date + ".csv", encoding= 'utf-8', index= False)
    print("wAcc Done!!")


    ### wGyr ###
    file_names_6 = glob("D:/KNIH병합하기병합하기나스에올리기/KNIH_MERGE_FOLD/S" + member + "/*wGyr.csv")
    total_6 = pd.DataFrame()
    print(file_names_6)

    for file_name_6 in file_names_6:
        try:
            temp_6 = pd.read_csv(file_name_6, sep=',',header= None, names= col_Load_List_wGyr, encoding='utf-8') 
        except:
            temp_6 = pd.read_csv(file_name_6, sep=',',header= None, on_bad_lines='warn', encoding='utf-8') 
            continue

        total_6 = pd.concat([total_6, temp_6]) 
        print(f"{file_name_6} is Done.")

    print("Let's GO!")
    total_6.to_csv(FILE_PATH + "_wGyr" + date + ".csv", encoding= 'utf-8', index= False)
    print("wGyr Done!!")


    ### wHR ###
    file_names_7 = glob("D:/KNIH병합하기병합하기나스에올리기/KNIH_MERGE_FOLD/S" + member + "/*wHR.csv")
    total_7 = pd.DataFrame()
    print(file_names_7)

    for file_name_7 in file_names_7:
        try:
            temp_7 = pd.read_csv(file_name_7, sep=',',header= None, names= col_Load_List_wHR, encoding='utf-8') 
        except:
            temp_7 = pd.read_csv(file_name_7, sep=',',header= None, on_bad_lines='warn', encoding='utf-8') 
            continue

        total_7 = pd.concat([total_7, temp_7]) 
        print(f"{file_name_7} is Done.")

    print("Let's GO!")
    total_7.to_csv(FILE_PATH + "_wHR" + date + ".csv", encoding= 'utf-8', index= False)
    print("wHR Done!!")


    ### wPre ###
    file_names_8 = glob("D:/KNIH병합하기병합하기나스에올리기/KNIH_MERGE_FOLD/S" + member + "/*wPre.csv")
    total_8 = pd.DataFrame()
    print(file_names_8)

    for file_name_8 in file_names_8:
        try:
            temp_8 = pd.read_csv(file_name_8, sep=',',header= None, names= col_Load_List_wPre, encoding='utf-8') 
        except:
            temp_8 = pd.read_csv(file_name_8, sep=',',header= None, on_bad_lines='warn', encoding='utf-8') 
            continue

        total_8 = pd.concat([total_8, temp_8]) 
        print(f"{file_name_8} is Done.")

    print("Let's GO!")
    total_8.to_csv(FILE_PATH + "_wPre" + date + ".csv", encoding= 'utf-8', index= False)
    print("wPre Done!!")

    print(f"{member} Done")


print(" ")
print("!!! ALL DONE !!!")

