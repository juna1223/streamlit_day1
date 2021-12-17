import streamlit as st
import numpy as np
import pandas as pd

# https://altair-viz.github.io/
import altair as alt

# https://plotly.com/python/
import plotly.express as px

def main() :
    df1 = pd.read_csv('data/lang_data.csv')
    st.dataframe(df1)

    print(df1.columns[ 1 :  ])

    lang_list = df1.columns[ 1 :  ]

    choice_list = st.multiselect('언어를 선택하세요', lang_list)

    print(choice_list)

    if len(choice_list) != 0 :
        # 유저가 선택한 언어만, 차트를 그리려고 합니다.
        df_selected = df1[choice_list]

        # 스트림릿이 제공하는 라인차트
        st.line_chart(df_selected)

        # 스트림릿이 제공하는 영역차트
        st.area_chart(df_selected)

    df2 = pd.read_csv('data/iris.csv')

    # 스트림릿이 제공하는 바차트
    df_selected2 = df2[ ['sepal_length', 'petal_length'] ]
    st.bar_chart(df_selected2)

    # Altair 이용!
    # x 축과 y 축 설정 + color 또는 size 로 차트를 풍성하게 표현
    chart = alt.Chart(df2).mark_circle().encode(
        x = 'petal_length',
        y = 'petal_width', 
        color = 'species'
    )
    st.altair_chart(chart)

    # 스트림릿의 map 챠트
    df3 = pd.read_csv('data/location.csv', index_col=0)
    st.dataframe(df3)

    st.map(data= df3)

    # plotly 를 이용한 차트 그리기
    df4 = pd.read_csv('data/prog_languages_data.csv', 
                                            index_col=0)
    st.dataframe(df4)

    # plotly의 pie 차트
    fig1 = px.pie(df4, 'lang', 'Sum', 
                            title='각 언어별 파이차트')
    st.plotly_chart(fig1)

    # plotly의 bar 차트

    df4_sorted = df4.sort_values('Sum', ascending=False)

    fig2 = px.bar(df4_sorted, x='lang', y='Sum')
    st.plotly_chart(fig2)

if __name__ == '__main__' :
    main() 