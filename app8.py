### 파일 업로드하는 방법 ####
import streamlit as st
from PIL import Image
import pandas as pd
import os
from datetime import date, datetime

# 디렉토리 정보와 파일을 알려주면, 해당 디렉토리에
# 파일을 저장하는 함수를 만들겁니다.
def save_uploaded_file(directory, file) :
    # 1.디렉토리가 있는지 확인하여, 없으면 디렉토리부터만든다.
    if not os.path.exists(directory) :
        os.makedirs(directory)
    # 2. 디렉토리가 있으니, 파일을 저장.
    with open(os.path.join(directory, file.name), 'wb') as f :
        f.write(file.getbuffer())
    return st.success("Saved file : {} in {}".format(file.name, directory))


def main() :
    st.title('파일 업로드 프로젝트')
    menu = ['Image', 'CSV', 'About']
    choice = st.sidebar.selectbox("메뉴", menu)

    if choice == 'Image' :
        st.subheader('이미지 파일 업로드')

        # 파일 업로드 코드 작성. 카피 앤 페이스트 해서 사용하세요.
        image_file = st.file_uploader("이미지를 업로드 하세요", type=['png','jpg','jpeg'])
        if image_file is not None :
            # 프린트문은 디버깅용으로서, 터미널에 출력한다.
            print(type(image_file))
            print(image_file.name)
            print(image_file.size)
            print(image_file.type)

            # 파일명을, 현재시간의 조합으로 해서 만들어보세요.
            # 현재시간.jpg
            current_time = datetime.now()
            print(current_time)
            print(current_time.isoformat().replace(':', '_'))
            current_time = current_time.isoformat().replace(':', '_')
            image_file.name = current_time + '.jpg'

            # 파일을 저장할 수 있도록, 위의 함수를 호출하자.
            save_uploaded_file('temp', image_file)

            # 파일을 화면에 나오게
            img = Image.open(image_file)
            st.image(img,use_column_width=True)


    elif choice == 'CSV' :
        st.subheader('CSV 파일 업로드')

        data_file = st.file_uploader("CSV 파일 업로드", type=['csv'])
        if data_file is not None :
            print(data_file.name)
            print(data_file.size)
            print(data_file.type)

            current_time = datetime.now()
            print(current_time)
            print(current_time.isoformat().replace(':', '_'))
            current_time = current_time.isoformat().replace(':', '_')
            data_file.name = current_time + '.csv'


            # 파일 업로드 함수를 호출만 하면 된다.
            save_uploaded_file('csv_files',  data_file )

            df = pd.read_csv(data_file)
            st.dataframe(df)

    elif choice == 'About' :
        st.subheader('파일 업로드 프로젝트 입니다.')


if __name__ == '__main__' :
    main()



elif choice == 'CSV' :
    st.subheader('CSV 파일 업로드')

    data_file = st.file_uploader("CSV 파일 업로드", type=['csv'])
    if data_file is not None,
        print(data_file.name)
        print(data_file.size)
        print(data_file.type)

        # 파일 업로드 함수를 호출만 하면 된다.
        save_uploaded_file('csv_files', data_file)

        df = pd.read_csv(data_file)
        st.dataframe(df)
if __name__ == '__main__' :
    main()