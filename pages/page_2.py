import streamlit as st
from streamlit_gsheets import GSheetsConnection

#ラジオボタン
source_d_type = st.radio(
        '情報データ元の種類',
        ('Gドライブのurl', 'csv直接入力')
)

with st.form(key='profile_form'):
        #テキストボックス
        # name = st.text_input('名前')

        url = st.text_input('Googleスプレッドシート（Gドライブのurl）')
        # conn = st.connection("gsheets", type=GSheetsConnection)
        conn = st.experimental_connection("gsheets", type=GSheetsConnection)

        # address = st.text_input('住所')
        csv = st.text_area('CSVデータなど')


        #ボタン
        submit_btn = st.form_submit_button('送信')
        cancel_btn = st.form_submit_button('キャンセル')
        if submit_btn:
                st.text(f'情報データ元の種類： {source_d_type}')
                # st.text(f'ようこそ{name}さん!{address}に書籍を送りました！')
                df = conn.read(spreadsheet=url)
                st.title("date&births")
                st.write(df)
                # st.text(f'年齢層： {age_category}')
