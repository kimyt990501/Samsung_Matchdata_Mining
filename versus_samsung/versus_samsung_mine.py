#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

# 한글 사용하기 위해 폰트 불러옴
plt.rc('font', family='Malgun Gothic')
from IPython.display import set_matplotlib_formats
set_matplotlib_formats('retina')

# 팀당 삼성 상대 승률 파일을 불러와 시각화 진행
data = pd.read_csv('C:\\Users\\user\\Desktop\\samsung_matchdata_mining\\Samsung_Matchdata_Mining\\data\\versus_samsung\\all_team_wr.csv', encoding='euc-kr')
data = data.astype({'승률':'float'})

sns.barplot(x = '승률', y = '팀명', data= data, orient= 'h')
plt.title('각 팀별 삼성 라이온즈 상대 승률')
# %%
