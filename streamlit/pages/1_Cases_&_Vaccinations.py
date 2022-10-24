#help from https://www.projectpro.io/recipes/add-file-uploader-widget-streamlit

import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt
from io import StringIO
import pandas as pd
import pickle
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


st.set_page_config(page_title="Hello!", layout='wide')

st.title(' Recent COVID Cases and Vaccination Analysis')
st.sidebar.image('./pages/images/choropleth.png', width=250)

# factor=st.selectbox("Let's Look!", options=['Cases','Vaccination'])

recent_cases=pd.read_csv('./pages/plotting/recent_total.csv')
recent_vacc=pd.read_csv('../streamlit/pages/plotting/additional_does_vax_pct_by_state.csv')
recent_vacc.rename(columns={'Location':'State','Additional_Doses_Vax_Pct':'Additional Doses Vacc %'}, inplace=True)
recent_cases.rename(columns={'No. of Cases (Mean)': 'No. of Cases'}, inplace=True)

######################US state map#####################

#Hospitalization rate visualization on country map
# Code adapted from :
#https://towardsdatascience.com/simplest-way-of-creating-a-choropleth-map-by-u-s-states-in-python-f359ada7735e
# https://stackoverflow.com/questions/72481189/plotly-map-choropleth-not-plotting-anything-streamlit
#https://discuss.streamlit.io/t/choropleth-width-and-height-changes-based-on-the-color-option/32132


def choropleth_plot(df, title):

    fig = px.choropleth(df,
                            locations=df.iloc[:,0],
                            locationmode="USA-states",
                            scope="usa",
                            color=df.iloc[:,1],
                            color_continuous_scale="Plasma_r",
                            height=700,
                            width = 700,

                            # labels={'color': title}
                            )

    fig.update_layout(
              title_text = title,
              title_font_family="Times New Roman",
              title_font_size = 14,
              title_font_color="black",
              title_x=0.45,
              margin={"r":0,"t":0,"l":0,"b":0},
              )


    # fig.update_traces(colorbar_orientation='h', selector=dict(type='choropleth'))
    # fig.show()
    st.plotly_chart(fig)
    return

#####################################################################

#State barh plotting#############



def barh_plot(df, title, xlabel, ylabel):
    figure, barh_ax=plt.subplots(figsize=(20,15))
    barh_ax.barh(df.iloc[:,0],df.iloc[:,1])
    barh_ax.set_title(title, size=20)
    barh_ax.set_xlabel(xlabel, size=20)
    barh_ax.set_ylabel(ylabel, size=20)
    # barh_ax.set_tickparams(labelsize=18)
    for i in barh_ax.patches:
        if i.get_width() >0:
            plt.text(i.get_width()+0.3, i.get_y()+0.4,
                     str(round((i.get_width()), 2)),
                     fontsize = 10, fontweight ='bold',
                     color ='grey');
        else:
            pass
    st.pyplot(figure)
    return



#######################################

container1 = st.container()
col1, col2 = st.columns(2)

with container1:
    with col1:
        st.write('### Cases')
        factor=st.selectbox("Select to see States with Highest or Lowest No. of Cases", options=['Highest No. of Cases','Lowest No. of Cases'])
        if factor=='Highest No. of Cases':
            st.write(recent_cases.head())
        else:
            st.write(recent_cases.dropna().tail())
        choropleth_plot(recent_cases, 'No. of Cases - September 2022')
        # barh_plot(recent_cases, 'No. of Cases \n September 2022', 'Count','State')
    with col2:
        st.write('### Vaccination')
        factor=st.selectbox("Select to see States with Highest or Lowest Vaccinated Population", options=['Highest Vacc Population','Lowest Vacc Population'])
        if factor == 'Highest Vacc %':
            st.write(recent_vacc.head())
        else:
            st.write(recent_vacc.tail())
        choropleth_plot(recent_vacc, 'Additional Doses Vaccination Pop(%) - September 2022')
        # barh_plot(recent_vacc, 'Additional Doses Vaccination Pop(%)', 'Count','State')

##############################
row2_1, row2_2 = st.columns((2, 1))
with row2_1:
    st.write('### Cases/Vaccination by State')
    factor=st.selectbox("Let's Look!", options=['No. of Cases','Vaccination'])
    if factor=='No. of Cases':
        barh_plot(recent_cases, 'No. of Cases \n September 2022', 'Count','State')
    else:
        barh_plot(recent_vacc, 'Additional Doses Vaccination Pop(%)', 'Count','State')
#######################################

st.markdown("""
<style>
.small-font {
    font-size:10px !important;
}
</style>
""", unsafe_allow_html=True)
st.markdown('<p class="small-font">Image credit:</p>', unsafe_allow_html=True)
st.markdown('<p class="small-font">https://medium.com/specialist-library-support/creating-a-choropleth-map-using-geopandas-and-financial-data-d0b0e51e55ea</p>', unsafe_allow_html=True)
