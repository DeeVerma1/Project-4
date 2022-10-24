#streamlit Help
#https://coderzcolumn.com/tutorials/data-science/basic-dashboard-using-streamlit-and-matplotlib#3
#https://blog.streamlit.io/designing-streamlit-apps-for-the-user-part-ii/
#https://discuss.streamlit.io/t/change-font-size-in-st-write/7606/2


import streamlit as st

st.set_page_config(page_title='Hello!', layout='wide' )

st.write('# Welcome to COVID data exploration page!')

st.sidebar.success("Select a page above!")

st.image('./pages/images/sars-cov-2.jpg')


################################################

st.markdown("""
<style>
.small-font {
    font-size:10px !important;
}
</style>
""", unsafe_allow_html=True)
st.markdown('<p class="small-font">Image credit:</p>', unsafe_allow_html=True)
st.markdown('<p class="small-font">https://hub.jhu.edu/2021/01/15/sars-cov-2-covid-19-variants-new-strains/</p>', unsafe_allow_html=True)
# st.write('https://images.search.yahoo.com/search/images;_ylt=AwrjZNg_b1Vj4NgrO.5XNyoA;_ylu=Y29sbwNncTEEcG9zAzEEdnRpZANMT0NVSTA1M0JfMQRzZWMDcGl2cw--?p=covid+images&fr2=piv-web&type=E211US105G0&fr=mcafee#id=63&iurl=https%3A%2F%2Fapi.hub.jhu.edu%2Ffactory%2Fsites%2Fdefault%2Ffiles%2Fstyles%2Fsoft_crop_2400%2Fpublic%2Fsars-cov-2_011521.jpg%3Fitok%3D9FoBICYo&action=click')
