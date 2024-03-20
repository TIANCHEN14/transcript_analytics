import streamlit as st
import json

# create an title for this thing
st.title('Radio Transcript Analytic Viewer')

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
        
        output_timing = 'line number : ' + str(round(seg[index]['id'] , 2)) + ' time : ' + str(round(seg[index]['start'] , 2)) + ' -- ' + str(round(seg[index]['end'] , 2))
        output_content = 'Text : ' + seg[index]['text']

        # here is the part to break down and pull information out of each segment
        st.markdown(output_timing)
        st.markdown(output_content)

        # divider
        #st.divider()