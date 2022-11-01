import csv
import os
import glob
import pymongo

DEPARTURE_PATH = ".\\data_folder\\user_folder"
DESTINATION_PATH = ".\\data_folder\\server_folder"
MEMBERS = ["604", "605", "606", "607", "608", "609", "610", "611", "612", "613", "614", "615", "616", "617", "618", "619", "620", \
    "621", "622", "623", "624", "625", "627", "628", "629", "630", "631", "632" ,"633", "634", "635", "636", "637", "638", "639", \
    "641", "643", "644", "645", "650", "651", "652", "653"]

def main(file_path_list, member, start_end_):
    for file in file_path_list:                                                     # 모든 DEPARTURE_PATH밑의 파일 리스트
        splited_file_path = file.split('\\')
        file_owner = splited_file_path[3]                                           # S606
        core_path = splited_file_path[6]                                            # 221010_Phone_Acc.csv
        core_path = core_path.split('.')[0].split('_')                              # [YYMMDD, Phone, Acc]
        dep_date = core_path[0][2:]; dep_dev = core_path[1]; dep_sen = core_path[2] # MMDD, Phone, Acc
        
        if dep_dev == "Phone":
            dep_dev = "Mobile"
        
        # print(file_owner)
        
        if member == file_owner:                                                    # Sxxx == S607
            destination_path = DESTINATION_PATH + '\\' + member + '\\' + start_end_ # .\\data_foler\\server_folser\\S607\\1010_1020
            dest_list = searchDesFile(destination_path)                             #./S607밑의 모든 파일 리스트    

            for dest_file in dest_list:                                             # 목적지 폴더에서 일치하는 파일 찾기
                des_splist_path = dest_file.split('\\')[5].split('_')               # [., data_folder, server_folder, S607, 1010_1020, 617_1020_wPre.csv]
                des_date = des_splist_path[1]; des_dev = des_splist_path[2][0]; des_sen = des_splist_path[2].split('.')[0][1:]

                if dep_date == des_date and dep_dev[0].lower() == des_dev and dep_sen[0] == des_sen[0]:     # 날짜, 디바이스, 센서 비교, 같다면
                    f_dep = open(file, "r+", encoding='UTF-8')            # 읽기 전용으로 출발지 파일 열기
                    line = f_dep.read().replace(",\"\n\"","")
                    f_dep.close()

                    f_dep_temp = open(file, "w", encoding='UTF-8')
                    f_dep_temp.write(line)
                    f_dep_temp.close()

                    f_dep = open(file, "r+", encoding='UTF-8')            # 읽기 전용으로 출발지 파일 열기
                    reader = csv.reader(f_dep)
                    f_des = open(dest_file, "a") # 쓰기로 도착지 파일 열기
                    writer = csv.writer(f_des)

                    for row in reader:
                        # print(row)
                        for i in range(len(row)):
                            row[i] = str(row[i])
                            if row[i] == '\n':
                                row[i] == ''
                        writer.writerow(row)
                else:
                    continue
        else:
            pass                                                                    # 넘김   

def searchDepFile(dir):
    files = glob.glob(dir + "\\**\\*.csv", recursive=True)
    return files
    
def searchDesFile(dir):
    files = glob.glob(dir + "\\**\\*.csv", recursive=True)
    # print(files)
    return files

if __name__ == "__main__":
    start_ = input("MMDD: ")
    end_ = input("MMDD: ")
    start_end_ = start_ + '_' + end_
    # print(start_end_)

    for member in MEMBERS:
        member = 'S' + member
        file_path_list = searchDepFile(DEPARTURE_PATH + '\\' + member + '\\' + start_end_)
        if len(file_path_list) == 0:
            continue
        else:
            # print(file_path_list[0].split('\\'))
            main(file_path_list, member, start_end_)
        print(f"DONE. {member}")
