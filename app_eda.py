import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns




def run_app_eda() :
    st.subheader('탐색적 데이터 분석')

    df = pd.read_csv('data/Car_Purchasing_Data.csv', encoding = 'ISO-8859-1')

    print(df)

    if st.checkbox('데이터 프레임 보기') :
        st.dataframe(df)

    st.subheader('기본 통계 데이터')
    st.dataframe(df.describe())

    st.subheader('최대 / 최소 데이터 확인하기')
    

    column = st.selectbox('컬럼을 선택하세요.', df.columns[ 3 : ] )  # gender컬럼부터 끝까지 목록으로 보여주세요

    st.text('최대 데이터')
    st.dataframe(df.loc[df[column] == df[column].max(),]) # 선택한 컬럼의 최대 데이터를 보여주세요.
    
    st.text('최소 데이터')
    st.dataframe(df.loc[df[column] == df[column].min(),]) # 선택한 컬럼의 최소 데이터를 보여주세요.

    st.subheader('컬럼 별 히스토그램')

    column = st.selectbox('히스토그램 확인할 컬럼을 선택하세요.', df.columns[ 3 : ] ) # selectbox는 중복으로 쓸때 에러가 난다. 위랑 다르게 작성해보자
    bins = st.number_input('빈의 갯수를 입력하세요.',10,30,20)

    fig = plt.figure()
    df[column].hist(bins=bins)
    plt.title(column + ' Histogram')
    plt.xlabel(column)
    plt.ylabel('count')

    st.pyplot(fig)

    st.subheader('상관 관계 분석')
    column_list = st.multiselect('상관분석을 하고싶은 컬럼을 선택하세요.', df.columns[ 3 : ] ) # 2개 이상이니 리스트로 받아진다!!
    
    if len(column_list) >= 2 :
        # df[column_list].corr()  ## 유저가 원하는 컬럼의 상관관계
        fig2 = plt.figure()
        sns.heatmap(data = df[column_list].corr(numeric_only=True), annot=True,
                    vmin=-1, vmax=1, cmap='coolwarm', fmt='.2f', linewidths=0.5)
        st.pyplot(fig2)


