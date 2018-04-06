# DataVisualizationW18
CMPUT 302  Winter 2018 Project 3

Best viewed in Chrome and Safari

## To Be Able To Run Our Site on a Local Server Follow These Steps
### Run these commands in order
Clone the master branch using:

    $ git clone https://github.com/DataVisualizationW18/DevRepo.git

Then navigate to the DevRepo directory in your command line

If you are using Linux or iOS run the command:

    $sudo pip3 install virtualenv 

If that doesn't work use: 

    $ sudo apt-get install python3-virtualenv)
  
Then Run:
  
    $ virtualenv venv

    $ . venv/bin/activate (On Windows: venv\Scripts\activate)

    $ pip3 install Flask
  
If you are using Windows run the command:

  $ pip3 install virtualenv

Then Run:
  
    $ virtualenv venv

    $ venv\Scripts\activate

    $ pip3 install Flask

### Documentation For Above Steps If Issues Encountered
[Install Flask](http://flask.pocoo.org/docs/0.12/installation/#installation)

### Install Program Dependencies With

In the same DevRepo directory run the following commands:

If you are using Linux or iOS:

    $ pip3 install xlrd

    $ sudo pip3 install pygal (or with: sudo apt-get install pygal)
    
If you are using Windows:

    $ pip3 install xlrd

    $ pip3 install pygal
  

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

We decided to not implement the FAQ section that we mentioned outline in our Discount Evaluation. We decided to ommit this for a few reasons.
1. We don't have time to test what common problems people might have or not have with our site and as a result we can not put together a comprehensive FAQ that would be helpful to the majority of the users. 
2. While we would like to add on into our UI, we don't know a great location for it to be placed within our UI. Also we did not have the oppurtunity to layout and analyze a FAQ section and aren't quite sure how it would fit into our UI design in a useful but aesthetically pleasing fashion.

We decided to avoid implementing visualizations within the History Tab, that would act as a preveiw to what visualization types were used at that point. We decided to omit this because when the buttons have more than one visualization on them it becomes very difficult to actually see which history event you want to click, as the details become very small and difficult to distinguish.
