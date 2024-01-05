# NemaApp
## Table of contents
1. [Introduction](#Introduction)
2. [Requirements](#Requirements)
3. [Running the App](#Running)
4. [Known Issues and Temporary Fixes](#Issues)


## Introduction <a name="Introduction"></a>
A simple deep learning nematode classifier Webapp developed using Flask web framework. The category is split into parasitic and non-parasitic nematode. The model used for parasitic identification is EfficientNetV2B0, while DenseNet201 is used for non-parasitic identification. <b>The models are not included in the repository.</b>

## Requirements <a name="Requirements"></a>
This app was built using Python 3.11.5. Make sure to have Python installed, preferably version 3.11.5. Using any other version might cause compatibility issues.

## Running the App <a name="Running"></a>
### First Run
For first run, use install.bat or install.sh, or install the modules manually by:
1. python -m venv venv / python3 -m venv venv
2. .\venv\scripts\activate / source venv/bin/activate
3. pip install -r requirements.txt (makse sure to read the requirements file first) / pip3 install -r requirements.txt
4. python main.py / python3 main.py

### Running the App Again
The modules only need to be installed once (normally). To run the program again, use runapp.bat / runapp.sh, or using the terminal by:
1. .\venv\scripts\activate / source venv/bin/activate
2. python main.py / python3 main.py

## Known Issues and Temporary Fixes <a name="Issues"></a>
1. bootstrap-flask causing problem (in Python 3.12)<br/>
   Fix: See requirements.txt and app.py. Comment the lines that has the following #Comment this if flask_bootstrap is causing issues

