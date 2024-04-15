import streamlit as st
import json 
import os

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
# Also this file will be able to have label and 
def transcript_disp(file_path):

    # file object handler
    f = open(file_path)
    
    # input all the file
    file_contect = json.load(f)

    # here is the part to read all the segment into an dataframe
    seg = file_contect['segments']

    # custom font size
    custom_style = 'font-size:20px'

    # define empty columns for the data labeler
    col1 = []
    col2 = []
    summary_collection = []

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

        # Data labeling part
        col1_temp , col2_temp = st.columns(2)
        col1.insert(index , col1_temp)
        col2.insert(index , col2_temp)
        radio_key_str = "radio_key_" + str(index)
        sum_key_str = "sum_key_" +str(index)


       # print(radio_key_str)



        # column 1 will be the left side GUI
        with col1[index]:
            st.radio("What Type of information is this",
                     ["Spotting" , "Vehicle handling" , "Track Info" , "General Info"],
                     key = radio_key_str
                     )
            
        with col2[index]:
           summary_collection.insert(index, st.text_input("Summary for this pargraph", 
                                                            key = sum_key_str,
                                                            )  )
           if summary_collection[index]:
               st.markdown("Summary is : " + summary_collection[index])

# load_data function to prevent everytime we interact with the webpage we will load the data again
@st.cache_data
def load_data(file_path):
    with open(file_path , "r" ) as f:
        return json.load(f)


# here is the part to handle dataset generation
def dataset_generator(file_path):
    

    
    # import the data set from the filepath if the file path has change
    # st.session_state.file_content is the dictionary object that we got from JSON file
    # st.session_state.file_path is the string for the dirtory where the file is at
    if "file_content"  not in st.session_state or st.session_state.file_path != file_path:
        st.session_state.file_content = load_data(file_path)
        st.session_state.file_path = file_path

    # create the segment object
    seg = st.session_state.file_content['segments']
    max_pages = len(seg)
    
    # Setup pagination
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 140
    if 'responses' not in st.session_state:
        st.session_state.responses = []
    
    # Display pagination controls
    col1, col2, col3= st.columns([1, 1 , 8])
    with col1:
        if st.button('Previous'):
            if st.session_state.current_page > 0:
                st.session_state.current_page -= 1
    with col2:
        if st.button('Next'):
            if st.session_state.current_page < max_pages - 1:
                current_text = seg[st.session_state.current_page]['text']
                current_option = st.session_state[f"radio_key_{st.session_state.current_page}"]
                current_summary = st.session_state[f"sum_key_{st.session_state.current_page}"]
                save_response(current_text, current_option , current_summary)

                st.session_state.current_page += 1
    with col3:
        if st.download_button('Export', data = json.dumps(st.session_state.responses, indent=4) , file_name = 'train_dataset.json' , mime = "application/json"):
            st.success('file export successfully')
    
    st.write(f"Page {st.session_state.current_page + 1} of {max_pages}")

    # Display the segment for the current page
    segment = seg[st.session_state.current_page]  # Access the current segment
    custom_style = 'font-size:20px'
    id_text = round(segment['id'], 2)
    start_time_text = round(segment['start'], 0)
    end_time_text = round(segment['end'], 0)

    output_timing = f"<span style='{custom_style}'>#{id_text:4} Time: {start_time_text:8} -- {end_time_text:8}</span>"
    text_body = segment['text']
    output_content = f"<span style='{custom_style}'> | {text_body}</span> "
    st.markdown(output_timing + output_content, unsafe_allow_html=True)

    # User inputs 
    radio_key_str = f"radio_key_{st.session_state.current_page}"
    sum_key_str = f"sum_key_{st.session_state.current_page}"

    selected_option = st.radio("What Type of information is this",
                               ["Spotting", "Vehicle handling", "Weather Info", "General Info"],
                               key=radio_key_str)
    summary = st.text_input("Summary for this paragraph", key=sum_key_str)    
    
    st.markdown(f"dataset length {len(st.session_state.responses)}")
    
    if st.button('Clear'):
        st.session_state.responses.clear()
    


    



def save_response(text, selected_option, summary):
    temp_dict = {
        'instruction' : 'Please summarized this line of text',
        'input': text,
        'clasiifer': selected_option,
        'output': summary}
    
    st.session_state.responses.append(temp_dict)




    


    
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

    #hide_st_style = """
    #            <style>
    #            #MainMeue {visibility: hidden;}
    #            footer {visibility: hidden;}
    #            header {visibility: hidden;}
    #            </style>                        
    #"""

    #st.markdown(hide_st_style, unsafe_allow_html=True)
    
    # title for the main body
    st.title('Training Dataset Generator')
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
        dataset_generator(selected_file)




    




if __name__ == '__main__':
    main()