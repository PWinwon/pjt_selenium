# Data Analysis Project - PWinwon

###### 																													- 그래픽 카드 구매 시기 예측

-----

#### 프로젝트 계획이유📈

>주변 지인이 그래픽 카드 추천을 하였을 때, 저는 막연히 지금 가격이 비싸니 나중에 가격이 떨어지면 살 것을 추천하였습니다. 가상화폐의 급격한 가격 상승과 채굴기를 만들기 위해 채굴업자들이 그래픽 카드를 대량 구매함으로써 그래픽 카드의 가격이 덩달아 같이 상승한 대란이 여러차례있었습니다. 사용자의 입장에서 가상화폐의 가격 데이터와 그래픽 카드의 가격 데이터를 바탕으로 데이터 분석을 통해 구매시기를 예측해 알려줄 수 있다면 좋곘다는 생각으로 프로젝트를 개발하게 되었습니다.
>
>이 프로젝트는 `selenium` 을 이용하여 웹크롤링을 통해 데이터를 수집하여, 데이터를 바탕으로 분석을 하고 그 결과를 웹과 앱에서 쉽게 볼 수 있도록 시각화 하는 것을 목표로 하고 있습니다. 제가 분석한 데이터를 통해 많은 사용자들이 그래픽 카드의 구매 시기를 예측하고 합리적인 소비가 이루어졌으면 좋겠습니다.

----

#### 진행상황📃

- [ ] 데이터 수집
  - [ ] 그래픽 카드 데이터
    - [x] 매일 업데이트 할 수 있도록 코드 작성
    - [ ] 봇을 활용해 매일 자동 업데이트 할 수 있는 방법 고려
    - [ ] 과거 데이터 직접 수집해서 정리
  - [ ] 가상화폐 데이터
    - [x] 매일 업데이트 할 수 있도록 코드 작성
- [ ] 데이터 분석
- [ ] 데이터 시각화
  - [ ] d3js

-----

#### 고민❓

- 그래픽 카드의 가격이 하루에도 여러번 바뀜. 데이터 업데이트 시간 고정
  - ~~매일 업데이트 할 수 있도록 코드 작성~~  >>  `gcd.py` `collect_gc.py`
  - 봇을 이용한 자동 고정된 시간 업데이트 고려
- 가상화폐 데이터 모듈화
  - ~~매일 업데이트 할 수 있도록 코드 작성~~ >> `selenium_coin.py`
  - ~~oop 적용~~ >> `cod.py` `collect_co.py` >> `cod.py` ~~약간의 수정필요~~ >> 수정을 했지만 아직 부족
- 그래픽 카드의 과거 가격 데이터
  - ~~직접 데이터를 수집해야함~~  >>  직접 데이터 수집 사이트 발견 추후 업데이트 예정
  - 1달 주기의 최저가격, 평균가격 등의 데이터만 수집가능 즉, 매일 변하는 데이터를 수집하기 힘듬
- 데이터 분석 방법
  - 수리모델링에서 배운 블랙숄츠 방정식
  - 이외의 방법을 잘모름.. 공부해야함
- 데이터 시각화
  - js 공부

----

### 2021/07/31

- 프로젝트 개발환경 구축
  - 가상환경 venv

- 가상화폐 데이터 수집 코드 작성
  - `selenium` 이용해 크롤링
  - 이더리움 데이터 수집해 테스트하기

>가상환경, selenium 등 처음 써보는 패키지와 기능들이 많아 생각보다 시간이 오래걸렸다. 조금 더 익숙해 지도록 공부를 더 하고, 처음인만큼 자주 테스트를 통해 오류가 발생하지 않도록 노력하자

----

### 2021/08/01

- 그래픽 카드 가격 데이터 수집 코드 작성
  - 과거 데이터는 크롤링으로 구하기 쉽지 않아 직접 사진이나 영상을 참고하여 타이핑
  - 8월 1일부터 매일 가격을 크롤링 하기 위한 코드 작성
  - 그래픽 카드 가격 수집 코드 oop를 사용해 모듈화

> 전날 가상화폐 가격의 데이터는 `selenium`을 이용한 크롤링으로 쉽게 구할 수 있었지만 과거의 데이터를 굳이 보여주지 않는 쇼핑몰의 특성상 그래픽 카드의 과거 가격을 크롤링으로 수집하기가 거의 불가능 하였다. 차선책으로 오늘부터 크롤링을 통해 매일 그래픽 카드의 가격을 수집할 수 있도록 코드를 구현하였고, 과거의 데이터를 알 수 있는 표 혹은 차트를 통해 직접 데이터를 타이핑으로 수집하기로 계획하였다.

----

### 2021/08/02

- 가상화폐 가격 데이터 수집 코드 수정
  - 가상화폐 종류 별로 수집하도록 수정
  - 가상화폐의 특성상 바로 전날의 데이터만 업데이트 하도록 수정
  - 가상화폐 가격 데이터 수집 코드 oop를 사용해 모듈화

>가상화폐 가격 데이터 코드 또한 이식성과 확장성을 고려하여 코드를 수정 보완하였다. 하지만 바로 전날의 데이터를 긁어오는 과정에서 데이터가 csv에 저장될 때 데이터가 깨지는 현상을 발견하고 다음에 수정보완 하고자 계획하였다. 남은 그래픽 카드의 과거 데이터를 직접 수집을 완료하여 분석 단계로 넘어가야 하기 때문에 분석 방법에 대한 고민과 공부가 더 필요할 것 같다.

----

### 2021/08/17

- 가상화폐 가격 데이터 수집 코드 수정
  - 매일 업데이트 되는 가격 데이터를 수정했으나 아직 부족한 부분이 많음
  - 원하는 데이터만 불러올 수 있도록 코드 수정이 필요함
- 과거 그래픽카드 가격 데이터 수집 완료
  - 직접 css 에 작성하여도 되는지 확인 후 데이터 작성 예정
  - python의 파일 입출력을 통해 css로 변환 예정

> 프로젝트를 진행함에 있어, 데이터 수집이 쉽지 않다는 것을 몸소 깨달았다. 특히 셀레니움을 이용해 원하는 데이터를 수집하는 과정에서 데이터의 구조를 조금 더 자세하게 확인해야 한다는 사실을 깨달았다. 과거 데이터를 수집하기위해 틈틈히 시간을 내어 여러 웹사이트와 쇼핑몰, 커뮤니티 사이트 등을 활용하여 많은 가격 데이터들을 수집하였고, 이를 활용하기 위한 방법을 모색해보아야 겠다.

-----

