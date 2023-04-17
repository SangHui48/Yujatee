import streamlit as st
from streamlit_extras.switch_page_button import switch_page


st.title("Yuja Fashion Reccomendation Sys")

with st.form("form_index", clear_on_submit=True):
    gender = st.radio('성별', ['남자', '여자'], index=0, horizontal=True)
    height = st.text_input('신장')
    weight = st.text_input('몸무게')
    age = st.text_input('나이')
    
    submit = st.form_submit_button('다음')
    if submit:
        choose_style()
            