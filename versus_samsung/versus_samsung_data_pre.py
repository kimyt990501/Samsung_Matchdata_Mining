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
samsung_all = pd.read_csv('C:\\Users\\user\\Desktop\\samsung_matchdata_mining\\Samsung_Matchdata_Mining\\data\\samsung_match_data\\all\\samsung_all.csv', encoding='euc-kr')
team_wr_list = []

## 롯데 승률
is_lotte = samsung_all['상대팀'] == '롯데'
versus_lotte = samsung_all[is_lotte]
versus_lotte.drop(["Unnamed: 0"], axis=1, inplace =True)
res_lotte = versus_lotte['결과'].count()
lotte_wins = len(versus_lotte.loc[versus_lotte['결과'] == 'lose'])
lotte_wr = '%0.3f' % float(lotte_wins / res_lotte)
temp = ['롯데', lotte_wr]
team_wr_list.append(temp)

## 한화 승률
is_hanhwa = samsung_all['상대팀'] == '한화'
versus_hanhwa = samsung_all[is_hanhwa]
versus_hanhwa.drop(["Unnamed: 0"], axis=1, inplace =True)
res_hanhwa = versus_hanhwa['결과'].count()
hanhwa_wins = len(versus_hanhwa.loc[versus_hanhwa['결과'] == 'lose'])
hanhwa_wr = '%0.3f' % float(hanhwa_wins / res_hanhwa)
temp = ['한화', hanhwa_wr]
team_wr_list.append(temp)

## LG 승률
is_lg = samsung_all['상대팀'] == 'LG'
versus_lg = samsung_all[is_lg]
versus_lg.drop(["Unnamed: 0"], axis=1, inplace =True)
res_lg = versus_lg['결과'].count()
lg_wins = len(versus_lg.loc[versus_lg['결과'] == 'lose'])
lg_wr = '%0.3f' % float(lg_wins / res_lg)
temp = ['LG', lg_wr]
team_wr_list.append(temp)

## 두산 승률
is_doosan = samsung_all['상대팀'] == '두산'
versus_doosan = samsung_all[is_doosan]
versus_doosan.drop(["Unnamed: 0"], axis=1, inplace =True)
res_doosan = versus_doosan['결과'].count()
doosan_wins = len(versus_doosan.loc[versus_doosan['결과'] == 'lose'])
doosan_wr = '%0.3f' % float(doosan_wins / res_doosan)
temp = ['두산', doosan_wr]
team_wr_list.append(temp)

## 기아 승률
is_kia = samsung_all['상대팀'] == 'KIA'
versus_kia = samsung_all[is_kia]
versus_kia.drop(["Unnamed: 0"], axis=1, inplace =True)
res_kia = versus_kia['결과'].count()
kia_wins = len(versus_kia.loc[versus_kia['결과'] == 'lose'])
kia_wr = '%0.3f' % float(kia_wins / res_kia)
temp = ['KIA', kia_wr]
team_wr_list.append(temp)


## SK, SSG 통합 승률
is_sk = samsung_all['상대팀'] == 'SK'
versus_sk = samsung_all[is_sk]
versus_sk.drop(["Unnamed: 0"], axis=1, inplace =True)
res_sk = versus_sk['결과'].count()
sk_wins = len(versus_sk.loc[versus_sk['결과'] == 'lose'])
sk_wr = '%0.3f' % float(sk_wins / res_sk)

is_ssg = samsung_all['상대팀'] == 'SSG'
versus_ssg = samsung_all[is_ssg]
versus_ssg.drop(["Unnamed: 0"], axis=1, inplace =True)
res_ssg = versus_ssg['결과'].count()
ssg_wins = len(versus_ssg.loc[versus_ssg['결과'] == 'lose'])
ssg_wr = '%0.3f' % float(ssg_wins / res_ssg)
sum = float(sk_wr) + float(ssg_wr)
sk_ssg_wr = '%0.3f' % float(sum / 2)
temp = ['SK, SSG', sk_ssg_wr]
team_wr_list.append(temp)

## NC 승률
is_nc = samsung_all['상대팀'] == 'NC'
versus_nc = samsung_all[is_nc]
versus_nc.drop(["Unnamed: 0"], axis=1, inplace =True)
res_nc = versus_nc['결과'].count()
nc_wins = len(versus_nc.loc[versus_nc['결과'] == 'lose'])
nc_wr = '%0.3f' % float(nc_wins / res_nc)
temp = ['NC', nc_wr]
team_wr_list.append(temp)

## KT 승률
is_kt = samsung_all['상대팀'] == 'KT'
versus_kt = samsung_all[is_kt]
versus_kt.drop(["Unnamed: 0"], axis=1, inplace =True)
res_kt = versus_kt['결과'].count()
kt_wins = len(versus_kt.loc[versus_kt['결과'] == 'lose'])
kt_wr = '%0.3f' % float(kt_wins / res_kt)
temp = ['KT', kt_wr]
team_wr_list.append(temp)

## 키움 (우리, 넥센) 통합 승률
is_woori = samsung_all['상대팀'] == '우리'
versus_woori = samsung_all[is_woori]
versus_woori.drop(["Unnamed: 0"], axis=1, inplace =True)
res_woori = versus_woori['결과'].count()
woori_wins = len(versus_woori.loc[versus_woori['결과'] == 'lose'])

is_heroes = samsung_all['상대팀'] == '히어로즈'
versus_heroes = samsung_all[is_heroes]
versus_heroes.drop(["Unnamed: 0"], axis=1, inplace =True)
res_heroes = versus_heroes['결과'].count()
heroes_wins = len(versus_heroes.loc[versus_heroes['결과'] == 'lose'])

is_nexen = samsung_all['상대팀'] == '넥센'
versus_nexen = samsung_all[is_nexen]
versus_nexen.drop(["Unnamed: 0"], axis=1, inplace =True)
res_nexen = versus_nexen['결과'].count()
nexen_wins = len(versus_nexen.loc[versus_nexen['결과'] == 'lose'])

is_kiwoom = samsung_all['상대팀'] == '키움'
versus_kiwoom = samsung_all[is_kiwoom]
versus_kiwoom.drop(["Unnamed: 0"], axis=1, inplace =True)
res_kiwoom = versus_kiwoom['결과'].count()
kiwoom_wins = len(versus_kiwoom.loc[versus_kiwoom['결과'] == 'lose'])

res_heroes = res_woori + res_heroes + res_nexen + res_kiwoom
heroes_wins = woori_wins + heroes_wins + nexen_wins + kiwoom_wins
heroes_wr = '%0.3f' % float(heroes_wins / res_heroes)
temp = ['키움(우리, 넥센)', heroes_wr]
team_wr_list.append(temp)

## 각 팀에서 구한 승률을 하나의 데이터 프레임에 저장
all_team_wr = pd.DataFrame(team_wr_list)
all_team_wr.columns = ['팀명', '승률']
#print(all_team_wr)
all_team_wr.to_csv('C:\\Users\\user\\Desktop\\samsung_matchdata_mining\\Samsung_Matchdata_Mining\\data\\versus_samsung\\all_team_wr.csv', encoding='euc-kr')