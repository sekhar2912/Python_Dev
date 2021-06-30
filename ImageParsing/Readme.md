# Product Name
This tool will parse the input json file for an image and extract all the co-ordinate information of the various object and it uses OpneCV library to  draw those object in the canvas.

a) It also create an output file [File Name - Output_file.json ] under data folder. 
   This output file is created based on as per requirement provided 

b) It creates "OutImage.jpg" file in data folder

## Pre-requisite
Linux:
    sudo apt update
    sudo apt install python3-opencv

    To verify the installation, import the cv2 module and print the OpenCV version:
    python3 -c "import cv2; print(cv2.__version__)"

Output - 3.2.0

Create a directory named data. This directory should be created at the same level where the python script is present

All the input file should be kept inside the data directory and the generated output .json file
will be created in the same directory

## Installation

NA

## Usage example

Run the python script by the below command.

python3 <Script_Name.py> <Input_FileName.json>

## Development setup

NA

## Release History

* 0.0.1
    * Initial Version 


