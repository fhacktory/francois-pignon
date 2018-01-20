virtualenv venv
source venv/bin/activate
pip install -r requirements.txt -t lib
deactivate
npm install
echo 'To start the project'
echo '1/ activate the venv'
echo '2/ run `dev_appserver app.yaml`'