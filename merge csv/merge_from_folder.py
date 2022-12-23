import os
import glob
import shutil as sh

class file_processing():
    def __init__(self ,**kwargs):
        if 'path' in kwargs.keys():
            self.path = kwargs['path']
        else:
            self.path = None

    def find_file_path_lv1(self):
        ### 대상 파일 경로 확인 ###
        file_list = glob.glob(path + '/*' )

        print('>>> file list lv1')
        for file in file_list:
            print(file)
        print('=' * 40)   

    def find_file_path(self , **kwargs):
        ### 대상 파일 경로 확인 ###
        if 'type' in kwargs.keys(): # 특정 타입의 파일 경로만
            type = '.' + kwargs['type']
            file_list = glob.glob(path + '/**/*' + type, recursive=True)

        else: # 하위 폴더의 파일 전체
            file_list = glob.glob(path + '/**/*' )

        print('>>> file list')
        for file in file_list:
            print(file)
        print('=' * 40)
        self.file_list =  file_list

    def file_move(self, move_path):
        ### 대상 파일 이동 ###
        for file in self.file_list:
            file_name = file.split('\\')[-1] # file_name = 파일명.type
            sh.move(file ,move_path + '/' + file_name)

        print('file move success.')

    def file_copy(self, copy_path):
        ### 대상 파일 복사 ###
        for file in self.file_list:
            file_name = file.split('\\')[-1] # file_name = 파일명.type
            sh.copy(file ,copy_path)

        print('file copy success.')

if __name__ == '__main__':

    dir_root_list = ["/KNIH_Val_1/S", "/KNIH_Val_2/S", "/KNIH_Val_3/S", "/KNIH_Val_4/S", "/KNIH_Val_5/S"]

    for dir_root in dir_root_list:
        
        for SID in range(600, 655):

            path = "D:/KNIH병합하기병합하기" + dir_root + str(SID)
            mv_path = "D:/KNIH병합하기병합하기/KNIH_MERGE_FOLD/S" + str(SID)

            if os.path.isdir(mv_path)==False:
                os.mkdir(mv_path)

            f = file_processing(path=path ,move_path = mv_path)
            f.find_file_path_lv1()
            f.find_file_path(type='csv')
            f.file_move(mv_path)
            # f.file_copy(mv_path)

            print("DONE\t" + str(SID))
        print("DONE\t" + dir_root)
