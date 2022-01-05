from sklearn.base import BaseEstimator
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 전처리 함수 정의
# Null 처리 함수
def fillna(df):
    df['Age'].fillna(df['Age'].mean(),inplace=True)
    df['Cabin'].fillna('N',inplace=True)
    df['Embarked'].fillna('N',inplace=True)
    df['Fare'].fillna(0,inplace=True)
    return df

# 불필요한 속성 제거 함수
def drop_features(df):
    df.drop(['PassengerId','Name','Ticket'],axis=1,inplace=True)
    return df

# 레이블 인코딩
def format_features(df):
    df['Cabin']=df['Cabin'].str[:1] # Carbin값의 첫번째 문자만 가져옴
    features=['Cabin','Sex','Embarked']
    for feature in features:
        le=LabelEncoder()
        le=le.fit(df[feature])
        df[feature]=le.transform(df[feature])
    return df

# 전처리 함수 호출
def transform_features(df):
    df=fillna(df)
    df=drop_features(df)
    df=format_features(df)
    return df

class MyDummyClassifier(BaseEstimator):
    # fit 메서드는 아무것도 학습하지 않음
    def fit(self,X,y=None):
        pass
    # sex 피처가 1이면 0, 그렇지 않으면 1로 예측
    def predict(self,X):
        pred=np.zeros((X.shape[0],1))
        for i in range(X.shape[0]):
            if X['Sex'].iloc[i] ==1:
                pred[i]=0
            else:
                pred[i]=1

        return pred

# 데이터 로딩, 가공, 테스트/학습 데이터 분리
df = pd.read_csv('titanic_train.csv')
y_df = df['Survived']
X_df = df.drop('Survived',axis=1)
X_df = transform_features(X_df)
X_train, X_test, y_train, y_test = train_test_split(X_df, y_df, test_size=0.2, random_state=1)

# Dummy Classifier 사용하여 학습/예측/평가
myclf=MyDummyClassifier()
myclf.fit(X_train,y_train)

mypredictions = myclf.predict(X_test)
print('정확도: {0:.4f}'.format(accuracy_score(y_test,mypredictions)))