import streamlit as st
import pandas as pd

st.title("파이썬 페이지 구축")

st.write("파이썬 웹 사이트 성공!")

uploaded_file = st.file_uploader("파일첨부",type=['csv'])
st.text_input("텍스트를 입력하세요")

df = pd.read_csv(uploaded_file)

st.success("파일 업로드 성공")

st.dataframe(df)

