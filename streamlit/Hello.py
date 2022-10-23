import streamlit as st

st.set_page_config(page_title='Hello!', layout='wide' )

st.write('# Welcome to COVID data exploration page!')

st.sidebar.success("Select a demo above")

st.image('./pages/images/sars-cov-2.jpg')
