# DataVisualizationW18
CMPUT 302  Winter 2018 Project 3

## To Be Able To Run A Local Server Follow These Steps
### Run these commands in order
sudo pip3 install virtualenv (If that doens't work on linux use: sudo apt-get install python3-virtualenv)

mkdir myproject

cd myproject

virtualenv venv

. venv/bin/activate (On Windows: venv\Scripts\activate)

pip3 install Flask

### Documentation For Above Steps If Encounter Issues
[Install Flask](http://flask.pocoo.org/docs/0.12/installation/#installation)

### Install Program Dependencies With
pip3 install xlrd

sudo pip3 install pygal or sudo apt-get install pygal

### Navigate to folder contatining project with app.py present

To run use: FLASK_APP=app.py FLASK_DEBUG=1 python3 -m flask run

### Special Notes
Our site can handle any Metric Data as long as it follows the conventions used by the Metric Data contained in our Repository

Our Metric Data has been modified in 2 spots

Sheet - Issue Data

Row 1359 and Row 1360

The given Library Name is a Github Repo Not the actual Library Name

We modified these Library Names to fit with the convention used by the rest of Issue Data
