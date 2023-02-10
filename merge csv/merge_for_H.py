import pandas as pd  
import glob  

UID = 644

target = 'C:/Users/cjh-1/Desktop/iwanttobreakfree/tasking/*/' + str(UID) + '.csv'
save_root = 'C:/Users/cjh-1/Desktop/iwanttobreakfree/merged/' + str(UID) + '.csv'

csv_list = glob.glob(target)
csv_list

# 파일 Union 선언
df = pd.DataFrame()  
for f in range(0, len(csv_list)): # 예를들어 202301, 202302 로 된 파일이면 2023_*  
    temp_df = pd.read_csv(csv_list[f])
    df = df.append(temp_df, ignore_index=True)

# 데이터갯수확인  
print(df.shape)
# 데이터 잘 들어오는지 확인  
# print(df)

# 결측치 변경
df.replace(-1, 0, inplace=True)

# 날짜 자릿수 변경
df = df.astype({'date':'int'})
df.loc[ (df['date'] < 999) & (df['date'] > 800) , 'date'] = 20220000 + df['date']
df.loc[ (df['date'] > 999) & (df['date'] < 1300) , 'date'] = 20220000 + df['date']
df.loc[df['date'] < 800, 'date'] = 20230000 + df['date']

# 컬럼 변경
df['user_id'] = 'S' + str(UID)
df = df[['date','user_id','All','mAcc','mGyr','mPre','mLi','wAcc','wGyr','wPre','wHR']]
df = df.rename(columns={'All': 'minimum_per'})

# 파일저장
df.to_csv(path_or_buf=save_root,
                 sep=',',
                 na_rep='0',
                 float_format = '%.2f', # 2 decimal places
                 index = False) # do not write index
