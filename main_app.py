import streamlit as st
from PIL import Image
from streamlit_gsheets import GSheetsConnection

#テキスト関連
st.title('サプーアプリ')
st.caption('これはサプーの動画用のテストアプリです')
#画像
image = Image.open('./data/supu.jpg')
st.image(image, width=500)



url = "https://docs.google.com/spreadsheets/d/1JDy9md2VZPz4JbYtRPJLs81_3jUK47nx6GYQjgU8qNY/edit?usp=sharing"

# Please replace st.experimental_connection with st.connection.
# st.experimental_connection を st.connection に置き換えてください。
# conn = st.experimental_connection("gsheets", type=GSheetsConnection)
conn = st.connection("gsheets", type=GSheetsConnection)


data = conn.read(spreadsheet=url, usecols=[0, 1])
st.dataframe(data)