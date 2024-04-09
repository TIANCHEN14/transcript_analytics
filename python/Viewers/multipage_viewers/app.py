##########################################
##      Multipage streamlit app         ##
##########################################


import streamlit as st
import json

# create an title for this thing
st.title('Radio Transcript Analytic Tool')

# Here is the page navigation menu
st.page_link("app.py" , label = 'Home', icon = '🏠')
st.page_link('pages/Simple Viewer.py' , label = 'Simple Viewer' , icon = '1️⃣')
st.page_link('pages/page2.py' , label = 'Under Construction' , icon = '🏗️')

