import streamlit as st
import os
import json



# scan directory function
def scan_directory(path):
    
    # scan the file directory and return an nested dictionary

    dir_dict = {'files' : [], 'directories' : {} }

    for item in os.listdir(path):
        
        # join the current directory
        items_path = os.path.join(path, item)

        # check to see if the item is file
        if os.path.isfile(items_path):
            dir_dict['files'].append(item)

        # nested function if it is an directory we call the scan_directory again
        elif os.path.isdir(items_path):
            dir_dict['directories'][item] = scan_directory(items_path)


    return dir_dict

# this function is used to display the json file 
def transcript_disp(file_path):

    # file object handler
    f = open(file_path)
    
    # input all the file
    file_contect = json.load(f)

    # here is the part to read all the segment into an dataframe
    seg = file_contect['segments']

    # custom font size
    custom_style = 'font-size:20px'

    # here is the part to print all the 
    for index, content in enumerate(seg):
        
        #output_timing = '#' + str(round(seg[index]['id'] , 2)) + ' TIME : ' + str(round(seg[index]['start'] , 0)) + ' -- ' + str(round(seg[index]['end'] , 2)) + " "
        id_text = round(seg[index]['id'] , 2)
        start_time_text = round(seg[index]['start'] , 0)
        end_time_text = round(seg[index]['end'] , 0)

        output_timing = f"<span style='{custom_style}'>#{id_text:4} Time: {start_time_text:8}  -- {end_time_text:8} </span>"
        
        #output_timing = '**' + output_timing + '**'
        text_body = seg[index]['text']
        output_content = f"<span style='{custom_style}'> | {text_body} </span> "

        # here is the part to break down and pull information out of each segment
        st.markdown(output_timing + output_content , unsafe_allow_html=True)



    
# this function is to display everything in an directory
def list_dir(dir_path):

    if os.path.exists(dir_path):
        return os.listdir(dir_path)
    else: 
        return[]



# here is the part of main function
def main():
    # data folder path 
    main_path = r"C:\Users\tchen\OneDrive - Stewart-Haas Racing\Documents\Python project\transcript_analytics\data"
    prev_car = ''

    hide_st_style = """
                <style>
                #MainMeue {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>                        
    """

    st.markdown(hide_st_style, unsafe_allow_html=True)
    
    # title for the main body
    st.title('Radio Transcript Analytic Viewer')
    st.sidebar.image('image/SHR_logo.png' , width = 250 )

    # drop down for the first level
    years = list_dir(main_path)
    selected_year = st.selectbox('Select Year' , [""] + sorted(years, reverse=True))

    # drop down for the second level
    event = []
    if selected_year:
        event = list_dir(os.path.join(main_path, selected_year))
    selected_event = st.selectbox('Select Event' , sorted(event))

    # drop down for the third level
    car = []
    if selected_event:
        car = list_dir(os.path.join(main_path, selected_year , selected_event))
    selected_car = st.selectbox('Select Car Number' , car)


    # here is the part to introduce the auto import 
    if selected_car:
        selected_file = os.path.join(main_path , selected_year , selected_event , selected_car)
        #st.write(selected_file)
        transcript_disp(selected_file)




    




if __name__ == '__main__':
    main()