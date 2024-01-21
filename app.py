import streamlit as st
import img2ascii
from PIL import Image
import requests

st.set_page_config(layout='wide')

with st.form('image_upload'):
    image_file = st.file_uploader('Upload Image')
    'OR'
    image_file_url = st.text_input('Enter Image URL')
    st.form_submit_button('Process Image')

input_area = st.container()
output_area = st.container()
    
img = None
if image_file:
    img = Image.open(image_file)
elif image_file_url:
    stream = requests.get(image_file_url, stream=True).raw
    img = Image.open(stream)

if img:
    input_area.subheader('Original Image')
    input_area.image(img)

    output_area.subheader('ASCII version')
    output_area.image(img2ascii.img2ascii_image(img))