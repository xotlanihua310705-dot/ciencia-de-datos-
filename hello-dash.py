import streamlit as st
import pandas as pd 
st.title("Luis E")
dataframe = pd.read_csv("https://raw.githubusercontent.com/adsoftsito/ciencia-datos/refs/heads/main/titanic.csv")
st.dataframe(dataframe)
st.write("by xotlanihua310705-dot")
