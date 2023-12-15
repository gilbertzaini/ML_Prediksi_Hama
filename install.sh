#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR"

python3 -m venv venv
source venv/bin/activate
pip3 install -r ./requirements.txt
python3 main.py
