import streamlit as st
import pandas as pd
import requests

st.set_page_config(layout="wide")

st.title('Key-less API Database Tool')

url = st.text_input('API Sample URL')
if url:
    resp = requests.get(url).json()
    view = st.checkbox('View API Result')
    if view:
        st.text(resp)
    col1, col2, col3, col4 = st.columns(4)
    df = pd.DataFrame(resp)
    count = len(df)
    if count > 1:
        limit = st.slider('Record Limit', 1, count, count, step=1)
        df = df.head(limit)
    with col1:
        search1 = st.text_input('Select Field to Search:')
    with col2:
        search2 = st.text_input('Search:')
    with col3:
        if search1 and search2:
            search3 = st.text_input('Select Field to Search:',key=2)
    with col4:
        if search1 and search2:
            search4 = st.text_input('Search:',key=3)
    if search1 and search2:
        if search3 and search4 and search1 != search3:
            try:
                df = df[(df[search1].str.contains(search2.lower()) | df[search1].str.contains(search2.capitalize())) & (df[search3].str.contains(search4.lower()) | df[search3].str.contains(search4.capitalize()))]
            except:
                pass
        else: 
            try:
                df = df[(df[search1].str.contains(search2.lower()) | df[search1].str.contains(search2.capitalize()))]
            except:
                pass
    stdf = st.dataframe(df)
