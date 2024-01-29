import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')

# 한글 사용하기 위해 폰트 불러옴
plt.rc('font', family='Malgun Gothic')
from IPython.display import set_matplotlib_formats
set_matplotlib_formats('retina')

# 각 연도별 경기가 있었던 기간 (월별)
# 01, 02, 03, 04, 06, 07, 11, 12, 16, 21, 22, 23
m_4_10 = range(4, 11)

# 05, 09
m_4_9 = range(4, 10)

# 10, 19
m_3_9 = range(3, 10)

# 08, 13, 14, 15, 17, 18
m_3_10 = range(3, 11)

# 20
m_5_10 = range(5, 11)

'''
# 데이터 불러오기
wr_list = []

for month in m_5_10:
    match = pd.read_csv('C:\\Users\\user\\Desktop\\samsung_matchdata_mining\\Samsung_Matchdata_Mining\\data\\samsung_match_data\\2020\\samsung_2020_' + str(month) + '_match_result.csv', encoding='euc-kr')
    # 승률 구해서 리스트에 저장
    res = match['결과'].count()
    wins = len(match.loc[match['결과'] == 'win'])
    wr = '%0.3f' % float(wins / res)
    temp = [str(month), wr]
    wr_list.append(temp)

# 데이터프레임 만들어서 월별 승률 저장
wr_2020 = pd.DataFrame(wr_list)
wr_2020.columns = ['월', '승률']
wr_2020 = wr_2020.set_index('월')
print(wr_2020)
wr_2020.to_csv('C:\\Users\\user\\Desktop\\samsung_matchdata_mining\\Samsung_Matchdata_Mining\\data\\samsung_winning_rate\\wr_2020.csv', encoding='euc-kr')
'''
'''
# 2001~2023년까지의 경기 데이터를 각 년도별로 합치기
samsung_base = pd.read_csv('C:\\Users\\user\\Desktop\\samsung_matchdata_mining\\Samsung_Matchdata_Mining\\data\\samsung_match_data\\2020\\samsung_2020_5_match_result.csv', encoding='euc-kr')
for month in m_5_10:
    samsung_concat = pd.read_csv('C:\\Users\\user\\Desktop\\samsung_matchdata_mining\\Samsung_Matchdata_Mining\\data\\samsung_match_data\\2020\\samsung_2020_'+ str(month) +'_match_result.csv', encoding='euc-kr')
    samsung_base = pd.concat([samsung_base, samsung_concat], ignore_index=True)
samsung_base.to_csv('C:\\Users\\user\\Desktop\\samsung_matchdata_mining\\Samsung_Matchdata_Mining\\data\\samsung_match_data\\all\\samsung_2020_all.csv', encoding='euc-kr')
#print(samsung_base)
'''
'''
# 각 년도 별 데이터를 하나의 파일로 합치기
samsung_base = pd.read_csv('C:\\Users\\user\\Desktop\\samsung_matchdata_mining\\Samsung_Matchdata_Mining\\data\\samsung_match_data\\all\\samsung_2001_all.csv', encoding='euc-kr')
for year in range(2001, 2024):
    samsung_concat = pd.read_csv('C:\\Users\\user\\Desktop\\samsung_matchdata_mining\\Samsung_Matchdata_Mining\\data\\samsung_match_data\\all\\samsung_'+ str(year) +'_all.csv', encoding='euc-kr')
    samsung_base = pd.concat([samsung_base, samsung_concat], ignore_index=True)

# 결측치 존재하는 행, 필요없는 칼럼 제거하기
index = samsung_base[samsung_base['결과'].str.contains('-')].index
samsung_base = samsung_base.drop(index)
samsung_base.drop(['Unnamed: 0', '날짜'], axis=1, inplace =True)

# 데이터프레임을 csv 파일로 내보내기
samsung_base.to_csv('C:\\Users\\user\\Desktop\\samsung_matchdata_mining\\Samsung_Matchdata_Mining\\data\\samsung_match_data\\all\\samsung_all.csv', encoding='euc-kr')
'''

# 각 구단 별 삼성 상대 승률 구하기
