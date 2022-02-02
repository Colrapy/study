머신러닝 (파이썬 머신러닝 완벽 가이드)
===============================
--------------------------
1. 파이썬 기반의 머신러닝과 생태계 이해
- 머신러닝 : 애플리케이션을 수정하지 않고도 데이터를 기반으로 패턴을 학습하고 결과를 예측하는 알고리즘 기법을 통칭.
- 머신러닝 분류
   - 지도학습 : 분류, 회귀, 추천시스템, 시각/음성 감지/인지, 텍스트 분석, NLP
   - 비지도학습 : 클러스터링, 차원 축소, 강화학습
- 주요 패키지 : numpy, pandas, matplotlib, seaborn, sklearn 등
  - numpy : 선형대수 기반 프로그램 쉽게 만들 수 있도록 지원, 행렬의 연산
  ```python
  import numpy as np
  ```
  - pandas : DataFrame을 통해 numpy보다 편한 데이터 핸들링 가능
  ```python
  import pandas as pd
  ```
2. 사이킷런으로 시작하는 머신러닝
- 사이킷런 : 머신러닝 라이브러리 중 가장 많이 사용, 머신러닝을 위한 매우 다양한 알고리즘과 개발을 위한 편리한 프레임워크, API 제공
- 교차 검증 : 데이터의 편증을 막기 위해 여러 세트로 구성된 학습, 테스트 데이터 세트와 검증 데이터 세트에서 학습과 평가를 수행하는 것 -> 고정된 데이터셋으로 평가를 하다보면 테스트 데이터에만 최적의 성능을 발휘할 수 있음

    - K 폴드 교차검증
    - Stratified K 폴드 : K 폴드의 불균형한 레이블 분포 문제를 해결 ex) 데이터셋을 나누었을 때 각 레이블의 비율이 일정하지 않으면 문제가 생김.
    - cross_val_score() : 교차검증을 더 간편하게 수행하는 API.
    - GridSearchCV : 교차검증과 최적 하이퍼 파라미터(세팅 값) 튜닝을 한 번에 가능.
- 전처리
  - 데이터 인코딩
    - 레이블 인코딩 : 카테고리 feature들을 0,1,2,3 등의 숫자로 변환하는 것
    - 원-핫인코딩 : feature 값의 유형에 따라 새로운 feature를 추가해 해당하는 컬럼에 1을 표시, 나머지는 0
    
  
  - 피처 스케일링

    - 표준화 : feature 각각이 평균이 0이고 분산이 1인 가우시안 정규 분포를 가진 값으로 변환하는 것 -> 서로 다른 feature의 크기를 통일하기 위해 크기를 변환해주는 작업
      - StandardScaler : 일반적인 표준화
      - MinMaxScaler : 데이터의 분포가 가우시안 분포가 아닌 경우
    - 정규화(Nomalizer) : 사이킷런 모듈은 선형대수에서의 정규화 개념, 개별 벡터의 크기를 맞추기 위해 변환, 개별 벡터를 모든 피처 벡터 크기로 나눠줌
    
[3. 평가](https://github.com/Jolppp/study/blob/main/minjae/ch03%ED%8F%89%EA%B0%80.ipynb)

[4. 분류](https://github.com/Jolppp/study/blob/main/minjae/ch04%EB%B6%84%EB%A5%98.ipynb)

[5. 회귀](https://github.com/Jolppp/study/blob/main/minjae/ch05%ED%9A%8C%EA%B7%80.ipynb)

[6. 차원 축소](https://github.com/Jolppp/study/blob/main/minjae/ch06%EC%B0%A8%EC%9B%90%EC%B6%95%EC%86%8C.ipynb)

[7. 군집화](https://github.com/Jolppp/study/blob/main/minjae/ch07%EA%B5%B0%EC%A7%91%ED%99%94.ipynb) 

[8. 텍스트 분석](https://github.com/Jolppp/study/blob/main/minjae/ch08%ED%85%8D%EC%8A%A4%ED%8A%B8%EB%B6%84%EC%84%9D.ipynb)

[9. 추천 시스템](https://github.com/Jolppp/study/blob/main/minjae/ch09%EC%B6%94%EC%B2%9C%EC%8B%9C%EC%8A%A4%ED%85%9C.ipynb)
