import streamlit as st
from main import classify
import sys
from PIL import Image
from classes import names
from exception import CustomException
import time
        

st.set_page_config(page_title = "Image Classification", page_icon = '🔮')


st.title("Image Classification for Object Recognition")

input_src = st.file_uploader("upload here", type=['png', 'jpeg', 'jpg'])

lst_object = list(names.values())
lst_object.sort()
lst_object = [obj.capitalize() for obj in lst_object]


if input_src:
    try:
        st.sidebar.title('Configuration')
        st.sidebar.multiselect('Objects', lst_object)

        button = st.button('Predict')
        if button:
            start_time  = time.time()
            classify(input_src)
            end_time = time.time()
            left, right = st.columns(2)
            with left:
                st.image(input_src)

            # img = classify(input_src)
            with right:
                st.image(Image.open('Assets/result.jpg'))
            
            #end_time = timing(1)
            #st.write(f'A Cat was identified at {end_time}')
            st.write('Time Taken : %.2f ms'%(end_time - start_time))
            st.success('Objects identified successfully')



    except Exception as e:
        raise CustomException(e, sys)