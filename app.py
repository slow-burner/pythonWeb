import streamlit as st
import pandas as pd

st.title("파이썬 페이지 구축")

st.write("파이썬 웹 사이트 성공!")

uploaded_file = st.file_uploader("파일첨부",type=['csv'])
st.text_input("텍스트를 입력하세요")
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.success("파일 업로드 성공")
  st.dataframe(df)
else:
  st.write("파일이 업로드 되지 않았습니다. 파일을 업로드해주세요")

