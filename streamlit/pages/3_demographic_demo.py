#help from https://www.projectpro.io/recipes/add-file-uploader-widget-streamlit

import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt
from io import StringIO
import pandas as pd
import pickle
import numpy as np

#Code adapted from :
#https://coderzcolumn.com/tutorials/data-science/basic-dashboard-using-streamlit-and-matplotlib#3


st.set_page_config(page_title="Hello!", layout='wide')

st.title('COVID Demographic Analysis')
# st.sidebar.success("Lets explore!")
st.sidebar.image('./pages/images/demographics.jpg', width=100)


case_count_sex=pd.read_csv('./pages/plotting/case_count_sex.csv')
case_count_race=pd.read_csv('./pages/plotting/case_count_race.csv')
case_count_ethnicity=pd.read_csv('./pages/plotting/case_count_ethnicity.csv')
case_count_age=pd.read_csv('./pages/plotting/case_count_age.csv')
case_count_race_norm=pd.read_csv('./pages/plotting/case_count_race_norm.csv')
case_count_ethnicity_norm=pd.read_csv('./pages/plotting/case_count_ethnicity_norm.csv')
case_count_age_norm=pd.read_csv('./pages/plotting/case_count_age_norm.csv')



def bar_plot(df, col):
    # figure, ax=plt.subplots(figsize=(4,6))
    # plt.figure(figsize=(4,6))
    bar_ax.bar( x=df.iloc[:-1,0], height=col[:-1], width=0.6, alpha=0.5)

    bar_ax.set_title(f'Cases by {df.columns[0].title()}', size=14)
    bar_ax.set_ylabel('Percentage', size=14)
    bar_ax.set_xticks(bar_ax.get_xticks())
    bar_ax.set_xticklabels(df.iloc[:-1,0], rotation=45, ha='right', rotation_mode='anchor')

    for i in bar_ax.patches:
        if i.get_height() >0:
            plt.text(i.get_x()+0.15, i.get_height()+0.4,
                     str(round((i.get_height()), 2)),
                     fontsize = 10, fontweight ='bold',
                     color ='grey');
        else:
            pass
    return

def bar_plot_norm(df,col):
    # figure, ax=plt.subplots(figsize=(4,6))
    bar_norm_ax.bar( x=df.iloc[:,0], height=col, width=0.6, alpha=0.5)

    bar_norm_ax.set_title(f'Cases by {df.columns[0].title()}\n Normalized by Population %', size=14)
    bar_norm_ax.set_ylabel('Normalized Percentage', size=14)
    bar_norm_ax.set_xticks(bar_norm_ax.get_xticks())
    bar_norm_ax.set_xticklabels(df.iloc[:,0], rotation=45, ha='right', rotation_mode='anchor')

    for i in bar_norm_ax.patches:
        if i.get_height() >0:
            plt.text(i.get_x()+0.1, i.get_height()+0.02,
                    str(round((i.get_height()), 2)),
                    fontsize = 10, fontweight ='bold',
                    color ='grey');
        else:
            pass

    return

st.sidebar.markdown("### Bar Chart: Cases")

bar_axis = st.sidebar.selectbox("Select Demographics of interest",
                                  options=['Gender','Age','Race','Ethnicity'])


if bar_axis:
    bar_fig=plt.figure(figsize=(3,4))
    bar_ax=bar_fig.add_subplot(111)
    if bar_axis=='Gender':
        bar_plot(case_count_sex, case_count_sex['percent'])
    elif bar_axis=='Age':
        bar_plot(case_count_age, case_count_age['percent'])
    elif bar_axis=='Race':
        bar_plot(case_count_race, case_count_race['percent'])
    elif bar_axis=='Ethnicity':
        bar_plot(case_count_ethnicity, case_count_ethnicity['percent'])

    bar_fig_norm=plt.figure(figsize=(3,4))
    bar_norm_ax=bar_fig_norm.add_subplot(111)
    if bar_axis=='Age':
        bar_plot_norm(case_count_age_norm,case_count_age_norm['norm_pct'])
    elif bar_axis=='Race':
        bar_plot_norm(case_count_race_norm,case_count_race_norm['norm_pct'])
    elif bar_axis=='Ethnicity':
        bar_plot_norm(case_count_ethnicity_norm,case_count_ethnicity_norm['norm_pct'])

##################### Layout Application ##################

container1 = st.container()
col1, col2 = st.columns(2)

with container1:
    with col1:
        bar_fig
    with col2:
        if bar_axis=='Age' or bar_axis=='Race' or bar_axis=='Ethnicity':
            bar_fig_norm


# container2 = st.container()
# col3, col4 = st.columns(2)

# with container2:
    # with col3:
        # hist_fig
    # with col4:
        # hexbin_fig
