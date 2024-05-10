import whisper
#from tkinter import Tk 
#from tkinter.filedialog import askopenfilenames, askdirectory
from pathlib import Path
import os
import json
import time

#Tk().withdraw()

# here is the part to open radio directory
radio_folder = './Data'

# here is the part to write an save directory
save_folder = './post'

# load whisper model
model = whisper.load_model('medium')

# start an timer
start_time = time.time()
cycle_timer = time.time()

# scan though the directory
for root, _, files in os.walk(radio_folder):
    for file in files:
        
        # check if the file is end with wav
        if file.endswith(".wav"):
            
            # join file path for whisper
            file_path = os.path.join(root, file)
            print(f'Transcribing : {file_path}')

            # transcribe the audio file
            result = model.transcribe(file_path)

            # generate json filename
            json_fname = os.path.join(save_folder , os.path.splitext(file)[0] + '.json')

            # json dump 
            with open (json_fname , 'w') as json_file:
                json.dump(result , json_file)

            # cycle complete
            print(f"Fully write into : {json_file}")
            
            # timer caluculator
            overall_time = time.time() - start_time
            cycle_time = time.time() - cycle_timer

            print('Total time use is ' , overall_time)
            print('Single time use is ' , cycle_time)
            

