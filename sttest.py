import streamlit as st

c1, c2= st.columns([50,20])


with c1:
    so = (st.text_input((""), key = '1' ))
    

with c2:
    st.write(so)







