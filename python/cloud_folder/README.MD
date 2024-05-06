# Whisper Transcripting
Instruction on how to use lambda lab cloud computing resources to transcrible weekly radio.

## Prepare cloud folder
Follow these steps:
1. Make an copy of template folder in this repository 
2. Copy all radio file into the data folder
3. Copy this folder to your local WSL folder
Mine is here /mnt/c/Users/tchen/Documents/cloud_sync/

## Cloud operation
Once you prepare the folder for WSL. Follow these steps:
1. Enter WSL on powershell
    ```sh
    wsl
    ```
2. Go to the folder we prepared earlier
    ```sh
    cd ~/Documents/cloud_sync/target_folder
    ```
3. Start rsync job to sync folder to lambda cloud
    - Locate your SSH keys in WSL
    - Find your username and server-IP for cloud
    ```sh
    rsync -av -e "ssh -i ~/SSH_KEY_LOCATION" TARGET_FOLDER USERNAME@SERVER_IP:REMOTE_SERVER_DIRECTORY
    ```
4. Open another instance of WSL and SSH into lambda GPU server
    ```sh
    wsl
    ssh -i KEY_LOCATION USERNAME@SERVER_IP
    ```
5. Go to the folder that just got synced to cloud and run following command, it will install all the required packages
    ```sh
    chmod +x install.sh
    ./install.sh
    ```
6. Run auto transcript file, for 40 files it normally takes about 2-4 hours
    ```sh
    python3 auto_transcript.py
    ```
7. After the program is done runing, we will need to sync everything back to local machine. We will go back to WSL terminal. NOT THE CLOUD TERMINAL!!!!!!!!!!!!!! Run following command
    ```sh
    cd TARGET_FOLDER/post
    scp -r -i SSH_KEY USERNAME@SERVER_IP:POST_SERVER_LOCATION .
    ```
    make sure the . is at the end
8. After the sync complete, make sure all files is at the local machine. Then we can terminate the cloud instance.
9. Now we need to sync all file to the company server. Run following commnad
    ```sh
    cd post
    mv post EVENTID
    rsync -av ./EVENTID COMPANY_SERVERNAME@SERVER_IP:TARGET_LOCATION
    ```
