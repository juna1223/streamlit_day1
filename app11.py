import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main() :
    st.title('Plotting with st.pyplot()')

    df = pd.read_csv('data/iris.csv')

    st.dataframe( df.head() )

    # 차트 그리기
    # sepal_length 와 sepal_width 의 관계를 차트로 그립니다.
    fig = plt.figure()
    plt.scatter(data= df, x='sepal_length', y='sepal_width')
    plt.title('sepal length vs width')
    plt.xlabel('sepal length')
    plt.ylabel('sepal width')
    st.pyplot(fig)

    fig2 = plt.figure()
    sns.regplot(data= df, x='sepal_length', y='sepal_width')
    st.pyplot(fig2)

    # sepal_length 로 히스토그램을 그려주세요.
    # bin의 갯수는 20개로 해주세요
    fig3 = plt.figure(figsize=(10,4))
    plt.subplot(1, 2, 1)
    plt.hist(data= df, x='sepal_length', bins = 10, rwidth=0.8)

    plt.subplot(1, 2, 2)
    plt.hist(data= df, x='sepal_length', bins = 20, rwidth=0.8)
    st.pyplot(fig3)

    # species 컬럼에는 종 정보가 들어있는데,
    # 각 종별로 몇개씩 있는지를 차트로 나타내시오.
    fig4 = plt.figure()
    sns.countplot(data= df, x = 'species')
    st.pyplot(fig4)

    # 데이터프레임의 차트 그리는 코드도 실행 가능!
    fig5 = plt.figure()
    df['species'].value_counts().plot(kind = 'bar')
    st.pyplot(fig5)

    fig6 = plt.figure()
    df['sepal_length'].hist()
    st.pyplot(fig6)

if __name__ == '__main__' :
    main() 