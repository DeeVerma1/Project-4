#help from https://www.projectpro.io/recipes/add-file-uploader-widget-streamlit

import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt
from io import StringIO
import pandas as pd
import pickle
import numpy as np


st.set_page_config(page_title="Hello!", layout='wide')

st.title(' Recent COVID Cases and Vaccination Analysis')
# st.sidebar.success("Lets click!")
factor=st.selectbox('Look!', options=['Cases','Vaccination'])

recent_cases=pd.read_csv('./pages/plotting/recent_total.csv')
# recent_total.sort_values(by ='No. of Cases (Mean)', ascending=False, inplace=True)

######################US state map#####################

#Hospitalization rate visualization on country map
# Code adapted from :
#https://towardsdatascience.com/simplest-way-of-creating-a-choropleth-map-by-u-s-states-in-python-f359ada7735e
#https://stackoverflow.com/questions/72481189/plotly-map-choropleth-not-plotting-anything-streamlit
def choropleth_plot(df, title):
    import plotly.express as px
    US_fig = (px.choropleth(df,
                        locations=df.iloc[:,0],
                        locationmode="USA-states",
                        scope="usa",
                        color=df.iloc[:,1],
                        color_continuous_scale="Plasma_r",
                        # labels={'act_participation_rate': 'ACT Participation Rate'}
                        ))
    US_fig.update_layout(
          title_text = title,
          title_font_family="Times New Roman",
          title_font_size = 14,
          title_font_color="black",
          title_x=0.45,
             )
    US_fig.show()
    return

#####################################################################

#State barh plotting#############



def barh_plot(y, width, title, xlabel, ylabel):
    # figure, ax=plt.subplots(figsize=(20,15))
    barh_ax.barh(y, width)
    barh_ax.set_title(title, size=20)
    barh_ax.set_xlabel(xlabel, size=20)
    barh_ax.set_ylabel(ylabel, size=20);
    # barh_ax.set_tickparams(labelsize=18)
    for i in barh_ax.patches:
        if i.get_width() >0:
            plt.text(i.get_width()+0.3, i.get_y()+0.4,
                     str(round((i.get_width()), 2)),
                     fontsize = 10, fontweight ='bold',
                     color ='grey');
        else:
            pass
    plt.show()
    return

if factor=='Cases':
    choropleth_plot(recent_cases, 'No. of Cases \n September 2022')
    st.plotly_chart(US_fig)

    barh_fig=plt.figure(figsize=(20,15))
    barh_ax=barh_fig.add_subplot(111)
    barh_plot(recent_total['State'],recent_total['No. of Cases (Mean)'],
            'Avg. No. of Cases \n September 2022', 'Count','State')
    st.pyplot(barh_fig)

# st.pyplot(US_fig)
#fig.write_image('../Images/ACT_participation_rate_by_state.jpg')
