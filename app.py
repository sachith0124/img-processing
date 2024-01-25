import streamlit as st
import img2ascii
from PIL import Image
import requests
import util
from st_click_detector import click_detector

st.title('Image 2 ASCII')

cols = st.columns([0.8, 0.2], gap='large')
with cols[0]:
    st.subheader('''
        :rainbow[An app that turns any Image to ASCII styled Image or Text.]''')
with cols[1]:
    st.link_button('Go to Dev\'s Website ↗️', url='https://sachith.streamlit.app/')

with st.form('image_upload'):
    c1, c2 = st.columns([0.8, 0.2], gap='small')
    with c1:
        image_file = st.file_uploader('Upload Image')
        st.markdown('<div style="text-align: center"> OR </div>', unsafe_allow_html=True)
        image_file_url = st.text_input('Enter Image URL')
        st.markdown('<div style="text-align: center"> OR </div>', unsafe_allow_html=True)
        with st.expander('Select from Sample Images', expanded=False):
            st.caption('Images may be subject to copyright. I do not own these images. \n Images are being dynamically loaded from an external source.')
            st.write("Click on image and click on 'Process Image' button!")
            image_file_url = click_detector(util.load_imgs_html())
            css='''
            <style>
                [data-testid="stExpander"] {
                    overflow: scroll;
                    height: 450px;
                }
            </style>
            '''
            st.markdown(css, unsafe_allow_html=True)
    with c2:
        options = list(img2ascii.AVAILABLE_IMAGE_MODES.keys()) + list(img2ascii.AVAILABLE_TEXT_MODES.keys())
        selected_mode = st.radio('Select Mode', options=options)
        process_img = st.form_submit_button('Process Image', use_container_width=True)

input_area = st.container()
output_area = st.container()
    
img = None
if image_file:
    img = Image.open(image_file)
elif image_file_url:
    stream = requests.get(image_file_url, stream=True).raw
    img = Image.open(stream)

if process_img and img:
    output_area.empty()
    with st.spinner('Processing Image...'):
        input_area.subheader('Original Image')
        input_area.image(img)

        output_area.subheader('ASCII version')
        if selected_mode in img2ascii.AVAILABLE_IMAGE_MODES:
            output_area.image(img2ascii.gen_ascii_image(img, mode=selected_mode))
        else:
            output_area.write('Development In Progress... Please Try Later!')