import streamlit as st
from PIL import Image

#テキスト関連
st.title('サプーアプリ')
st.caption('これはサプーの動画用のテストアプリです')
#画像
image = Image.open('./data/supu.jpg')
st.image(image, width=500)
