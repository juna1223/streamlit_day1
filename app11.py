import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main() :
    st.title('Plotting with st.pyplot()')

    df = pd.read_csv('data/iris.csv')

    st.dataframe(df.head())

    # 차트그리기
    # sepal_length 와 sepal_width 의 관계를 차트로 그립니다.
    fig = plt.figure()
    plt.scatter(data= df, x='sepal_length', y = 'sepal_width')
    plt.title('sepal length vs width')
    plt.xlabel('sepal length')
    plt.ylabel('sepal width')
    st.pyplot()






if __name__ == '__main__' :
    main()