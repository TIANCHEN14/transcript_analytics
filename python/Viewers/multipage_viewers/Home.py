##########################################
##      Multipage streamlit app         ##
##########################################


import streamlit as st
import json

#set the browser as widemode
st.set_page_config(page_title= "Radio Analytic Tool",
                   page_icon= '📻' , 
                   layout = 'wide' , 
                   menu_items={
                       'About' : 'Stewart Haas Racing 2024'

})

hide_st_style = """
                <style>
                #MainMeue {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>                        
"""

st.markdown(hide_st_style, unsafe_allow_html=True)

# create an title for this thing
st.title('Radio Transcript Analytic Tool')
st.sidebar.image('image/SHR_logo.png' , width = 250 )

# Here is the page navigation menu
st.page_link("Home.py" , label = 'Home', icon = '🏠')
st.page_link('pages/Single Car Viewer.py' , label = 'Single Car Viewer' , icon = '1️⃣')
st.page_link('pages/File Preview.py' , label = 'File Preview' , icon = '📁')
st.page_link('pages/Dataset Generator.py' , label = 'Under Construction' , icon = '🏗️')

