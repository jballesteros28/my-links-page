source .venv\script\activate
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
reflex init
reflex export --frontend-only
rm -rf public
unzip frontend.zip -d frontend
rm -f frontend.zip
deactivate