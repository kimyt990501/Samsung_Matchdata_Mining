# Samsung_Matchdata_Mining
파이썬을 통해 한국 프로야구 팀인 삼성 라이온즈의 역대 경기 기록을 통한 여러가지 분석 진행

## 프로젝트 목록

### 1. 삼성 라이온즈는 왜 '여름성' 이라고 불리는가
- 삼성 라이온즈의 별명인 '여름성'이 과연 사실에 근거한 별명인지 알아보는 프로젝트
- 데이터는 <https://www.koreabaseball.com/Schedule/Schedule.aspx> KBO 공식 홈페이지에서 크롤링 해옴
- ![summersung](https://github.com/kimyt990501/Samsung_Matchdata_Mining/assets/50610894/9c0958b0-0fb0-4782-afa6-8183e53e49ca)

#### 파일 명
- samsung_matchdata_crawling.py (크롤링을 위해 작성한 파일)
- samsung_winning_rate.py (승률 계산 후 파일 저장)
- samsung_matchdata_mine.py (데이터 불러와 시각화)

#### 개발환경
- IDE: Visual Studio Code
- Version: python 3.8

#### 기술 스택
- 언어: Python

#### 절차
- KBO 공식 홈페이지에서 삼성 라이온즈의 경기결과를 2001년부터 2023년까지 전부 크롤링해와 csv 파일로 저장하여 분석 시작
- 데이터 전처리
  - 월별 승패 결과를 뽑아서 승률을 구한 후 하나의 파일로 합친다
  - 월별 승률의 평균을 구하여 새로운 파일에 저장한다 (10월은 경기 일자가 적어 결과에 영향을 줄 수 있으므로 생략한다)
- 전처리한 파일의 '월' '승률' 칼럼을 선 그래프의 각 y, x로 두고 그래프를 그린다
- 그래프를 확인하여 승률 분석을 한다

#### 결론
- ![samsung_winningrate](https://github.com/kimyt990501/Samsung_Matchdata_Mining/assets/50610894/d46c1800-342b-407f-8dbd-1ab2219ddb9a)
- 그래프의 결과를 확인했을때 3, 4 월의 경기 승률은 4할 이하에 분포되어있지만 여름이 시작되는 5월 부터 4할을 넘어서더니 한창 여름인 6, 7, 8월엔 4할을 꾸준히 넘으며 여름 끝물인 9월엔 거의 5할 가까이 오르기도 한다는 사실을 알게 되었다
- 따라서 '여름성' 이라는 별명은 사실에 근거한다는 것을 알게 되었다.
### 2. 삼성 라이온즈에 강한 상대, 약한 상대는 각각 어느 팀인가
- 삼성 라이온즈의 상대 전적을 통해 역대 삼성 상대로 가장 잘했던, 가장 못 했던 팀은 각각 어느 팀인지 알아보는 프로젝트
- 데이터는 첫번째 프로젝트에서 크롤링해온 데이터를 그대로 사용한다
- 데이터 출처: <https://www.koreabaseball.com/Schedule/Schedule.aspx>

#### 파일 명
-

#### 개발환경
- IDE: Visual Studio Code
- Version: python 3.8

#### 기술 스택
- 언어: Python
