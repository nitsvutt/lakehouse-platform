# source python env
. myenv/Scripts/Activate.ps1

# upgrade pip
python -m pip install --upgrade pip

# install jupyter notebook
pip install notebook

# start jupyter notebook
jupyter notebook --no-browser --port 8977