# 스트림릿 라이브러리를 사용하기 위한 임포트문 작성.

# 스트림릿 라이브러리는 이미 설치했다!!
# pip install streamlit

# 위의 라이브러리는 설치했으므로, 임포트만 하면 된다.
import streamlit as st

# 웹 대시보드 개발 라이브러리인 스트림릿은
# main 함수가 있어야 한다.

def main() :
    st.title('Hello Streamlit. 웹 대시보드')
    st.title('헬로우')


if __name__ == '__main__' :
    main()
