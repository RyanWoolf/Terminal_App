#!/bin/bash
if [[ -x "$(command -v python3 --version)" ]]
then
    source ../.venv/bin/activate
    if [[ -x "$(command -v python3 -m art help)" ]]
    then 
        python3 main.py
        deactivate
    else
        python3 -m pip install art==5.7
        python3 main.py
        deactivate
    fi
else
    echo "
    You have lower version of Python or don't have Python3 yet. 

    Please visit "https://www.python.org/downloads/" to download the latest version. 

    Then try again.
    " >&2
fi
