import streamlit as st

def main():
    st.title('웹 대시보드')
    st.text('웹 대시보드 개발하기')

    name = '홍길동'

    st.text('제 이름은 {}입니다.'.format(name))

    st.header('이 영역은 헤더 영역')
    st.subheader('이 영역은 subheader 영역')

    st.success('성공했을 때의 메세지 영역')
    st.warning('이 영역은 경고 영역')
    st.info('정보를 보여주고 싶을 때')
    st.error('문제가 발생했음을 알려주고 싶을 때')
    
    st.help(range)
    st.help(sum)


if __name__ == '__main__' :
    main()
