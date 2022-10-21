#help from https://www.projectpro.io/recipes/add-file-uploader-widget-streamlit

import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt
from io import StringIO

st.set_page_config(
    page_title="Hello!"

)

st.title('Main Page')
st.sidebar.success("Lets click!")

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
