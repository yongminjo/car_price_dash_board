import streamlit as st
import numpy as np  # 이력서 작성시에 어떤것을 임포트해서 사용했는지 상세하게 적는게 좋다
import joblib


def run_app_ml() :
    st.subheader('자동차 금액 예측')

    # 성별, 연봉, 카드빚, 자산을
    # 유저한테 입력받는다.
    gender = st.radio('성별 선택', ['남자', '여자'])

    if gender == '남자':
        gender = 0
    else :
        gender = 1

    age = st.number_input('나이 입력',18,100)

    salary = st.number_input('연봉 입력',5000,1000000)

    debt = st.number_input('카드빚',0,1000000)

    worth = st.number_input('자산 입력',1000,10000000)
        # 이렇게 입력받은 이유는 이 항목들로 학습시켰기 때문이다.

    if st.button('금액 예측') :
        new_data = np.array([gender, age, salary, debt, worth]) #고객 정보를 입력받는다
        new_data = new_data.reshape(1,5) # 넘파이 2차원 데이터로 변환시킨다.
        regressor = joblib.load('model/regressor.pkl') # 모델을 불러온다
        y_pred = regressor.predict(new_data) 

        price = round(y_pred[0])

        # print(str(price)+'달러짜리 차량 구매 가능합니다.')
        # print(f'{price}달러짜리 차량 구매 가능합니다.') # 포맷팅방법 1
        # print('{}달러짜리 차량 구매 가능합니다.'.format(price)) # 포맷팅 방법 2

        st.subheader(f'{price}달러짜리 차량 구매 가능합니다.') # 서브헤더로 글씨를 더욱 키운다.

    # 버튼을 누르면 예측한 금액을 표시한다.
