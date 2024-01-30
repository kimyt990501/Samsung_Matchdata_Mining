# Samsung_Matchdata_Mining
파이썬을 통해 한국 프로야구 팀인 삼성 라이온즈의 역대(2001~2023년) 경기 기록을 통한 여러가지 분석 진행

## 프로젝트 목록

### 1. 삼성 라이온즈는 왜 '여름성' 이라고 불리는가
- 삼성 라이온즈의 별명인 '여름성'이 과연 사실에 근거한 별명인지 알아보는 프로젝트
- 데이터는 <https://www.koreabaseball.com/Schedule/Schedule.aspx> KBO 공식 홈페이지에서 크롤링 해옴
- ![summersung](https://github.com/kimyt990501/Samsung_Matchdata_Mining/assets/50610894/9c0958b0-0fb0-4782-afa6-8183e53e49ca)

#### 파일 명
- samsung_matchdata_crawling.py (크롤링을 위해 작성한 파일)
- summersung_winningrate.py (승률 계산 후 파일 저장)
- summersung_mine.py (데이터 불러와 시각화)

#### 개발환경
- IDE: Visual Studio Code
- Version: python 3.8

#### 기술 스택
- 언어: Python

#### 절차
- KBO 공식 홈페이지에서 삼성 라이온즈의 경기결과를 2001년부터 2023년까지 전부 크롤링해와 csv 파일로 저장하여 분석 시작
- 데이터 전처리
- 전처리한 파일의 '월' '승률' 칼럼을 선 그래프의 각 y, x로 두고 그래프를 그린다
- 그래프를 확인하여 승률 분석을 한다

#### 데이터 전처리 과정
- KBO 공식 홈페이지에서 데이터를 크롤링하기 위해서는 해당 사이트의 페이지 소스를 가져와야 했다, 하지만 해당 사이트가 동적사이트였기 때문에 BeautifulSoup4 와 Selenium 을 같이 썼다
- 우선 Selenium 으로 동적 사이트의 페이지 소스를 가져와 BeautifulSoup4 로 해당 소스를 'html parser' 를 통해 파싱하였고 그걸 사용해서 데이터를 크롤링하였다
- 오로지 삼성의 경기 데이터만 가져와야 했기 때문에 여러가지 조건을 달아줘야 했다.
  - 역대 삼성의 구장인 대구 시민구장, 포항 야구장, 대구 라이온즈파크 이 세 곳을 조건으로 달아서 삼성의 상대팀명만 가져오게 했다
  - 경기가 취소된 경우는 스코어 데이터가 없기 때문에 '우천취소', '그라운드 사정' 같이 경기 취소 사유를 코드에 조건으로 달아두었다
- 참고로 해당 파일의 열은 '월', '상대팀명', '결과' 총 세개이다
- 위 조건을 달아 뽑아온 삼성 경기 데이터를 사용하여 월별 승률을 구해 연도별 승률 데이터 파일을 생성하고 해당 파일들을 전부 합쳐주었다
- 승률 데이터 파일의 열은 '월', '승률' 이렇게 두개이다
- 이 승률 데이터 파일을 통해 시각화 및 분석을 진행하였다 (10월엔 경기 횟수도 적고 결과에 영향을 끼칠수도 있기 때문에 생략함)

#### 결론
- ![summersung_wr](https://github.com/kimyt990501/Samsung_Matchdata_Mining/assets/50610894/ff12627b-ce71-413d-b199-a5b499073750)
- 그래프의 결과를 확인했을때 3, 4 월의 경기 승률은 5할 이하에 분포되어있지만 여름이라고 여겨지는 5, 6, 7, 8월엔 성적이 좋은 편이며 그중에서도 5월, 7월은 승률이 5할1푼 이상까지 올라가는 모습을 보인다, 하지만 8월엔 승률이 4할8푼 이하로 떨어지며 주춤하다가 여름의 끝물인 9월에 다시 5할 가까이 오르며 '여름성'의 면목을 보여준다
- 따라서 삼성 라이온즈는 5, 6, 7, 9월에 강하며 '여름성' 이라는 별명은 아마도 여름이 시작되는 5월, 한창 여름인 7월 그리고 여름이 끝나가는 9월에 성적이 좋았기때문에 붙여진 별명인것 같다.
- 물론 한창 여름인 8월엔 성적이 하락하는 것으로 보아 '여름성'이라는 별명은 100%맞는건 아닌것 같다
- 하지만 확실히 봄인 3, 4월엔 약하다.

### 2. 삼성 라이온즈에 강한 상대, 약한 상대는 각각 어느 팀인가
- 삼성 라이온즈의 상대 전적을 통해 역대 삼성 상대로 가장 강했던, 가장 약했던 팀은 각각 어느 팀인지 알아보는 프로젝트
- 데이터는 첫번째 프로젝트에서 크롤링해온 데이터를 그대로 사용한다
- 데이터 출처: <https://www.koreabaseball.com/Schedule/Schedule.aspx>

#### 파일 명
- versus_samsung_data_pre.py (데이터 전처리를 위한 파일)
- versus_samsung_mine.py (데이터 시각화 및 분석을 위한 파일)

#### 개발환경
- IDE: Visual Studio Code
- Version: python 3.8

#### 기술 스택
- 언어: Python

#### 절차
- 삼성은 왜 '여름성'인가 프로젝트에서 사용한 데이터 파일을 그대로 사용
- 해당 데이터 파일을 전처리
- 전처리한 파일을 토대로 '승률', '팀명'칼럼을 각각 막대 그래프의 x축 y축으로 두고 그래프를 그린다
- 그래프를 보며 분석

#### 데이터 전처리 과정
- 이전 프로젝트에서 썼던 데이터 파일을 그대로 가져와 전처리 진행
- 각 팀마다 삼성 상대로 승률이 어떤지를 보는 것이기 때문에 모든 파일들을 합친 후 필요없는 칼럼은 삭제 ('날짜' 칼럼 삭제)
- 합친 파일을 불러와 각 팀에 해당하는 경기 수를 구하고 해당 팀이 이긴 횟수를 조건 '결과' == 'lose' 로 두어 구한다 (해당 파일은 삼성 기준이기 때문에 '결과' 가 'lose' 인 경기가 해당 팀이 이긴 경기 )
- 이긴 횟수 / 경기 수 연산을 통해 해당 팀의 삼성 상대 승률을 구하고 '팀명', '승률' 칼럼을 가진 데이터프레임을 새로 만들어 csv 파일로 내보낸다
- SK는 SSG의 전신팀이기 때문에 하나의 팀으로 묶었고
- 우리, 넥센, 키움을 하나의 팀으로 묶어서 계산했다 (해당 팀의 전신이라고 불리는 현대 유니콘스는 해체 하였기 때문에 기록에서 제외함)

#### 결론
- ![versus_samsung_wr](https://github.com/kimyt990501/Samsung_Matchdata_Mining/assets/50610894/4c021775-5f1b-4510-b4f8-fe1fd375bcab)
- 막대 그래프를 보아 알 수 있듯이 다들 비등비등하지만 그 중에서도 '한화'는 삼성 상대로 4할 이하의 승률을 보이며 'SK 및 SSG'는 삼성 상대로 5할이 넘는 승률을 보인다.
- 따라서 2001~2023년 경기 기록을 기준으로 봤을때
- 삼성 상대로 가장 약한 팀은 '한화' 이며
- 삼성 상대로 가장 강한 팀은 'SK, SSG' 이다
- 실제로 삼성은 ssg 상대로 경기 할 때 유독 약한 모습을 보이곤 했었다.. 물론 그 반대로 한화 상대론 강했던 기억이 있다
