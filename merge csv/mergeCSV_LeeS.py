import csv
import os
import glob

DEPARTURE_PATH = ".\\additional_Data"
DESTINATION_PATH = "."
# MEMBERS = ["608","609","610","611","612","619","620","621","622","623","624","625","637","630","631","643","644","645","601","602","650","651","652","653"]
MEMBERS = ["608","609","610","611","612","619","620","621","622","623","624","630","631","643","644","650","651","652","653"]
# MEMBERS = ["601","602","608","609","610","611","612","619","620","621","622","623","624","625","630","631","637","643","644","645","650","651","652","653"]


def main(file_path_list, member):
    for file in file_path_list:                                                 # 모든 DEPARTURE_PATH밑의 파일 리스트
        splited_file_path = file.split('\\')
        file_owner = splited_file_path[2]                                       # S606
        core_path = splited_file_path[3]                                        # KNIH_221003
        core_path = core_path.split('.')[0].split('_')                          # [YYMMDD, Phone, Acc]
        dep_date = core_path[0][2:]; dep_dev = core_path[1]; dep_sen = core_path[2] # MMDD, Phone, Acc

        if dep_dev == "Phone":
            dep_dev = "Mobile"

        if member == file_owner:                                                # Sxxx == S607
            destination_path = DESTINATION_PATH + '\\' + member                 # .\\S607
            dest_list = searchDesFile(destination_path)                         #./S607밑의 모든 파일 리스트    

            for dest_file in dest_list:                                                 # 목적지 폴더에서 일치하는 파일 찾기   
                des_splist_path = dest_file.split('_')                                  # [S606, MMDD, mAcc]      
                des_date = des_splist_path[1]; des_dev = des_splist_path[2][0]; des_sen = des_splist_path[2].split('.')[0][1:]

                if dep_date == des_date and dep_dev[0].lower() == des_dev and dep_sen[0] == des_sen[0]:     # 날짜, 디바이스, 센서 비교, 같다면
                    f_dep = open(file, "r+", encoding='UTF-8')      # 읽기 전용으로 출발지 파일 열기
                    line = f_dep.read().replace(",\"\n\"","")
                    f_dep.close()

                    f_dep_temp = open(file, "w", encoding='UTF-8')
                    f_dep_temp.write(line)
                    f_dep_temp.close()

                    f_dep = open(file, "r+", encoding='UTF-8')
                    reader = csv.reader(f_dep)
                    f_des = open(destination_path+ '\\' + dest_file, "a")
                    writer = csv.writer(f_des)

                    for row in reader:
                        print(row)
                        for i in range(len(row)):
                            row[i] = str(row[i])
                            if row[i] == '\n':
                                row[i] == ''
                        writer.writerow(row)
                else:
                    continue
        else:
            pass                                                                    # 넘김   

def searchFile(dir):
    files = glob.glob(dir + "\\**\\*.csv", recursive=True)
    return files

def searchDesFile(dir):
    for (path, dir_dir, files) in os.walk(dir):
        return files

if __name__ == "__main__":
    # kkt_path = DEPARTURE_PATH
    dep_path_list = []
    file_path_list = searchFile(DEPARTURE_PATH + '\\' + MEMBERS)
    print(file_path_list)
    for member in MEMBERS:
        main(file_path_list, member)
        print(f"DONE. {member}")
