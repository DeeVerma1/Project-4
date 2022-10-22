#help from https://www.projectpro.io/recipes/add-file-uploader-widget-streamlit

import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt
from io import StringIO
import pandas as pd
import pickle
import numpy as np


st.set_page_config(
    page_title="Hello!"
)

st.title('Time Plot of COVID Case Counts')
st.sidebar.success("Lets click!")

#####################################################################
###############No. of Cases Timeplot by state################################
# help from https://coderzcolumn.com/tutorials/data-science/basic-dashboard-using-streamlit-and-matplotlib

# st.sidebar.markdown("### Explore Time plot of Monthly Cases by state : ")

df_state_hosp_total=pd.read_csv('./pages/plotting/state_hospt_total.csv')

states_select=['PA', 'MI', 'NJ', 'MO', 'FL', 'LA', 'MD', 'CO', 'TX',
       'IL', 'OH', 'WI', 'SC', 'NY', 'VA', 'NC',
       'CA', 'IN',
       'GA']

state=st.selectbox('Select the state', options=states_select)

if state:
     fig=plt.figure(figsize=(10,4))
     plt.plot(df_state_hosp_total['case_month'],df_state_hosp_total[state], label=state)
     plt.title('Time plot of Monthly Cases')
     plt.ylabel('Case count', size=12)
     xlabel=df_state_hosp_total['case_month'].map(lambda x: str(x).rsplit('-',1))
     plt.xticks(label= xlabel, size=10, rotation=90)
     # plt.tick_params(labelrotation=90)
     plt.legend()
     plt.show()
     st.pyplot(fig)
     # xc
# avg_breast_cancer_df = breast_cancer_df.groupby("target").mean()
# bar_axis = st.sidebar.multiselect(label="Average Measures per Tumor Type Bar Chart",
                                  # options=measurements,
                                  # default=["mean radius","mean texture", "mean perimeter", "area error"])

# if bar_axis:
    # bar_fig = plt.figure(figsize=(6,4))

    # bar_ax = bar_fig.add_subplot(111)

    # sub_avg_breast_cancer_df = avg_breast_cancer_df[bar_axis]

    # sub_avg_breast_cancer_df.plot.bar(alpha=0.8, ax=bar_ax, title="Average Measurements per Tumor Type");

# else:
    # bar_fig = plt.figure(figsize=(6,4))

    # bar_ax = bar_fig.add_subplot(111)

    # sub_avg_breast_cancer_df = avg_breast_cancer_df[["mean radius", "mean texture", "mean perimeter", "area error"]]

    # sub_avg_breast_cancer_df.plot.bar(alpha=0.8, ax=bar_ax, title="Average Measurements per Tumor Type");
#
    #####################################################################

# def load_image(image_file):
    # img=Image.open(image_file)


#
