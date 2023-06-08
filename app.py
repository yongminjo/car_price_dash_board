import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from app_home import run_app_home
from app_eda import run_app_eda
from app_ml import run_app_ml

def main():

    st.title('🚘 자동차 가격 예측기')

    menu = ['🏠 Home', '🔍 EDA(탐색적 데이터 분석)', '🤖 ML(머신러닝)']

    choice = st.sidebar.selectbox('✅ 이용하실 메뉴를 선택하세요!', menu)

    if choice == menu[0] :
        run_app_home()

    elif choice == menu[1] :
        run_app_eda()
    
    else :
        run_app_ml()



if __name__ == '__main__':
    main()