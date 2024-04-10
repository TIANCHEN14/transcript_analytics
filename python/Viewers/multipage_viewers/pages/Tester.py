import streamlit as st
import json

# create an title for this thing
st.title('Radio Transcript Analytic Viewer')
st.sidebar.image('image/SHR_logo.png' , width = 250 )

#hide header in the production version
hide_st_style = """
                <style>
                #MainMeue {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>                        
"""

st.markdown(hide_st_style, unsafe_allow_html=True)

# file upload block and import
upload_filename = st.file_uploader('Choose an radio transcript file' , type = ['json'])

# import the json file from whisper
if upload_filename is not None:
    
    # input all the file
    file_contect = json.load(upload_filename)

    # here is the part to read all the segment into an dataframe
    seg = file_contect['segments']

    # here is the part to print all the 
    for index, content in enumerate(seg):
        
        output_timing = '#' + str(round(seg[index]['id'] , 2)) + ' TIME : ' + str(round(seg[index]['start'] , 2)) + ' -- ' + str(round(seg[index]['end'] , 2))
        output_timing = '**' + output_timing + '**'
        output_content = ' | TEXT : ' + seg[index]['text']

        # here is the part to break down and pull information out of each segment
        st.markdown(output_timing + output_content)
        #st.markdown(output_content)

        # divider
        #st.divider()