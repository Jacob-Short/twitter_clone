# Twitter_Clone

Building a small clone of Twitter. It will feature logged in users, a customized homepage, a tweet composing page, the ability to follow other users, and more.


There will be four pieces to this application, each with their own app:

*   config <--  project folder
*   twitteruser <-- This is a custom user app!
*   tweet <-- corresponding to the tweets
*   authentication <-- relating to auth/login/signup
*   notification <-- handling notifications for follows/mentions


Each app will (potentially) need its own:

*   models.py
*   views.py
*   urls.py
*   forms.py
*   \_\_init\_\_.py

# Twitter_Clone

I am building a clone of the social media site Twitter! It will feature signing up for an account, logging in, a customized homepage and profile, a page to compose tweets, and the ability to follow and interact with other users.


## Getting Started

These instructions will give you a copy of the project up and running on
your local machine for development and testing purposes. See deployment
for notes on deploying the project on a live system.

### Prerequisites

Requirements for the software and other tools to build, test and push 
- [Poetry](https://python-poetry.org/)
- [Python](https://www.python.org/)

### Installing

A step by step series of examples that tell you how to get a development
environment running

Download and install poetry 

    Windows

        (Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -

    Mac OS/ Linux

        curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

Avtivate virtual environment

    poetry shell

Install dependencies

    poetry install

Start server

    python manage.py runserver


## Built With

  - [Python](https://www.python.org/) - Used
    for the Code of Conduct
  - [Django](https://www.djangoproject.com/) - Used to choose
    the license


## Authors

  - **Jacob Short** 


  - **Billie Thompson** - *Provided README Template* -
    [PurpleBooth](https://github.com/PurpleBooth)





