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

### Documentation For Above Steps If Issues Encountered
[Install Flask](http://flask.pocoo.org/docs/0.12/installation/#installation)

### Install Program Dependencies With
pip3 install xlrd

sudo pip3 install pygal (or with: sudo apt-get install pygal)

### Navigate to folder contatining project with app.py present

To run use: FLASK_APP=app.py FLASK_DEBUG=1 python3 -m flask run

### Special Notes
Our site can handle any Metric Data as long as it follows the conventions used by the Metric Data contained in our Repository

Our Metric Data has been modified in 2 spots

Sheet - Issue Data

Row 1359 and Row 1360

The given Library Name is a Github Repo Not the actual Library Name

We modified these Library Names to fit with the convention used by the rest of Issue Data

# UI Changes from our Project Description or Results from Evaluation Testing

We decided to not implement the FAQ section that we said we would outline within our Discount Evaluation. We decided to ommit this UI choice for a few reasons.
1. We don't have time to test what common questions and problems people might have or not have with our site and as a result we can not put together a comprehensive FAQ that would be helpful to the majority of the users.
2. While we would like to add on into our UI, we don't know a great location for it to be placed within our UI. Also we did not have the oppurtunity to design how the FAQ section would look like or where it would fit within the current UI when opened.

We decided to avoid implementing visualizations within the History Tab. We decided this course of action because when the visualizations have more than one appearing within each history button, it becomes very difficult to actually see which history you want to click as the details become very small and difficult to distinguish.
