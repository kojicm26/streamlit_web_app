import streamlit as st
from PIL import Image
from streamlit_gsheets import GSheetsConnection

#テキスト関連
st.title('サプーアプリ')
st.caption('これはサプーの動画用のテストアプリです')
#画像
image = Image.open('./data/supu.jpg')
st.image(image, width=100)


url = "https://docs.google.com/spreadsheets/d/1JDy9md2VZPz4JbYtRPJLs81_3jUK47nx6GYQjgU8qNY/edit?usp=sharing" #サンプル(date&births)

conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read(spreadsheet=url, usecols=["date"])
st.title("date&births")
st.write(df)
