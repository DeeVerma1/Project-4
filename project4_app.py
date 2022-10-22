#help from https://www.projectpro.io/recipes/add-file-uploader-widget-streamlit

import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt
from io import StringIO
import pandas as pd
import pickle

X_train_dummies=pd.read_csv('./models/X_train_dummies.csv')
X_train_dummies=X_train_dummies.iloc[:,0]
X_train_dummies=list(X_train_dummies)

st.set_page_config(
    page_title="Hello!"
)

st.title('Main Page')
st.sidebar.success("Lets click!")

#filepath to our pickeled model
with open('models/demo_model.pkl','rb') as pickle_model:
    model=pickle.load(pickle_model)

# State=st.text_input('Please enter your location:', max_chars=500)
# Age=st.text_input('Please enter your age group:', max_chars=500)
# Gender=st.text_input('Please enter your gender (M/F):', max_chars=500)
# Race=st.text_input('Please enter your race:', max_chars=500)
# Ethnicity=st.text_input('Please enter your ethnicity:', max_chars=500)
# Month=st.text_input('Please enter month:', max_chars=500)

State = st.selectbox('Select your state',options= ['PA', 'MI', 'NJ', 'MO', 'LA', 'CO', 'TX',
'IA', 'IL', 'WA', 'OH','WI', 'MN', 'CT', 'SC', 'NY', 'VA', 'AL', 'NC', 'MA', 'NM', 'NV','CA',
'OK', 'AZ', 'NH', 'OR', 'TN', 'AR', 'MD', 'GA', 'ID', 'IN', 'FL', 'KS', 'UT', 'MT', 'KY', 'WY',
'ME', 'DC', 'VT', 'AK', 'HI'])

Age=st.selectbox('Select your age group',options= ['18 to 49 years', '65+ years', '50 to 64 years', '0 - 17 years'])

Gender=st.selectbox('Select your gender',options= ['Male','Female'])

Race=st.selectbox('Select your Race', options=['White', 'Black', 'Asian', 'American Indian/Alaska Native',
       'Multiple/Other', 'Native Hawaiian/Other Pacific Islander'])

Ethnicity=st.selectbox('Select your ethnicity', options=['Non-Hispanic/Latino', 'Hispanic/Latino'])

Month=st.selectbox('Select the month of the year', options=[1,2,3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

#Add text to predcition
X=pd.DataFrame({'res_state': State, 'age_group': Age, 'sex': Gender, 'race': Race, 'ethnicity': Ethnicity, 'month':Month}, index=[0])
features=['res_state','age_group','sex','race','ethnicity','month']
#dummyfying columns:
df_dum=pd.get_dummies(data=X, drop_first=True)

#Removing additional dummy columns
for col in df_dum.columns:
    if ("_" in col) and (col.rsplit("_",1)[0] in features) and col not in X_train_dummies:
        # print("Removing additional feature {}".format(col))
        df_dum.drop(col, axis=1, inplace=True)

#Adding missing columns
for col in X_train_dummies:
    if col not in df_dum.columns:
        # print("Adding missing feature {}".format(col))
        df_dum[col] = 0

df_dum=df_dum[X_train_dummies]

if st.button('Predict'):
    predicted_hosp=model.predict(df_dum)
    #Write out your prediction
    st.write(f'You may be at risk of hosp {predicted_hosp}')


def load_image(image_file):
    img=Image.open(image_file)
    return img


st.title("File Upload Tutorial")





image_file = st.file_uploader("Upload Images", type=["png","jpg","jpeg"])

if image_file is not None:

			  # To See details
			file_details = {"filename":image_file.name, "filetype":image_file.type,
                              "filesize":image_file.size}
			st.write(file_details)

              # To View Uploaded Image
			st.image(load_image(image_file),width=250)


# def process_img(img):
    # resize image (1 channel used for example; 1 for gray-scale, 3 for RGB-scale)
    # img_data = np.empty((299,299, 3), dtype=np.float32)
    # img_data = resize(img, output_shape=(299, 299, 3), preserve_range=True)
    # img_data = img_data.astype('float32')
    # img_data /= 255
    # img_data = img_data.reshape(1, 299, 299, 3)


    # save to numpy array



def main():
    menu=["Image"]
    choice=st.sidebar.selectbox("Menu",menu)

    if choice == "Image":
        st.subheader("Image")



#adding a file uploader

# file = st.file_uploader("Please choose a file")

# if file is not None:

    #To read file as bytes:

    # bytes_data = file.getvalue()

    # st.write(bytes_data)
