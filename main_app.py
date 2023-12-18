import streamlit as st
from PIL import Image
from streamlit_gsheets import GSheetsConnection

url = "https://docs.google.com/spreadsheets/d/1JDy9md2VZPz4JbYtRPJLs81_3jUK47nx6GYQjgU8qNY/edit?usp=sharing"

conn = st.connection("gsheets", type=GSheetsConnection)
