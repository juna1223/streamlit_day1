import streamlit as st
import pandas as pd
# 이미지 처리를 위한 라이브러리
from PIL import Image


def main():
    
    img = Image.open('data/image_03.jpg')
    print(img)
    st.image(img)

    st.image(img, use_column_width=True)

    st.image('https://w.namu.la/s/45507892b4f48b2b3d4a6386f6dae20c28376a8ef5dfb68c7cc95249ec358e3e68df77594766021173b2e6acf374b79ce02e9eeef61fcdf316659e30289e123fbddf6e5ec3492eddbc582ee5a59a2ff5d6ee84f57ad19277d179b613614364ad')
    
    video_file = open('data/video1.mp4', 'rb')
    st.video(video_file)
    
if __name__ == '__main__' :
    main()