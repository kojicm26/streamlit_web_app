import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Create a connection object.
# conn = st.connection("gsheets", type=GSheetsConnection)
conn = st.experimental_connection("gsheets", type=GSheetsConnection)

df = conn.read()
st.title("pet.ss")
st.write(df)
