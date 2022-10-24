import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt
from io import StringIO
import pandas as pd
import pickle
import numpy as np
import plotly.express as px

###############No. of Cases Timeplot by state################################
# help from https://coderzcolumn.com/tutorials/data-science/basic-dashboard-using-streamlit-and-matplotlib

# st.sidebar.markdown("### Explore Time plot of Monthly Cases by state : ")
st.set_page_config(page_title="Time plot", layout='wide')

st.title(' COVID Evolution')
st.sidebar.image('./pages/images/time_plot.png', width=100)


df_newcases=pd.read_csv('./pages/plotting/covid_cases_us_clean.csv')


time_fig=px.choropleth(df_newcases,
              locations = 'state',
              color="new_case",
              animation_frame='submission_date',
              color_continuous_scale="sunset",
              locationmode='USA-states',
              scope="usa",
              range_color=(0, 10009),
              title='Timeline Covid Cases In US by State',
              height=600
             )

st.plotly_chart(time_fig)


df_newcases['submission_date']=pd.to_datetime(df_newcases['submission_date'])
df_newcases.set_index('submission_date', inplace=True)
df_newcases.sort_index(inplace=True)

states_select=['AS', 'NYC', 'AL', 'GU', 'DC', 'NV', 'TX', 'KS', 'FL', 'KY', 'NM',
       'MD', 'CA', 'PW', 'CO', 'UT', 'OK', 'IN', 'MS', 'NE',
       'ND', 'MO', 'MI', 'HI', 'IA', 'MT', 'MN', 'PA', 'AR', 'VI', 'ME',
       'VA', 'NH', 'WV', 'OR', 'TN', 'CT', 'SC', 'WI', 'RI', 'GA', 'ID',
       'WY', 'NY', 'WA', 'AZ', 'OH', 'LA', 'DE', 'MP', 'MA', 'NC', 'NJ',
       'AK', 'PR', 'VT', 'SD', 'IL']
states_select.sort()

state=st.selectbox('Select the state', options=states_select)

if state:
     df_state=pd.DataFrame(df_newcases[df_newcases['state']==state].groupby('submission_date')['new_case'].aggregate(sum))
     df2=df_state.resample('W').sum()
     # fig=plt.figure(figsize=(12,4))
     # plt.plot(df2,label=state)

     fig = px.area(df2, x=df2.index, y=df2['new_case'])

     fig.update_layout(title='New Cases-weekly',
                    yaxis_title='Case count',
                    xaxis_title='Submission Date')

     st.plotly_chart(fig)
################################################
