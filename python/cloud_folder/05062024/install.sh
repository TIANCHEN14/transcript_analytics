#!/bin/bash

# update and install ffmpeg
echo "Updating and installing ffmpeg..."
sudo apt update && sudo apt install ffmpeg

# install nvtop
echo "Installing nvtop..."
sudo apt install nvtop

# install rust setup tool
echo "Installing rust setup tool"
pip3 install setuptools-rust

# install whisper OpenAI
echo "Install whisper..."
pip install git+https://github.com/openai/whisper.git

echo "Install complete"


