# SUCAL
Sorbonne Université calendar (unofficial)

[![Build Status](https://travis-ci.com/AmineDjeghri/SUCAL.svg?branch=master)](https://travis-ci.com/AmineDjeghri/SUCAL)

![Logo](images/logo_1200.png?raw=true "Optional Title")
# Features
- a fast website that loads your calendar in less than second compared to more than 25sec on the official website
- mobile responsive & better design
- account authentification to save your calendar 
- receive a notification to tell you 10min before a course where it is


# Want to contribute ?

# Installation
(brouillon !!!)
#### pipenv or your virtual env
Inside the SUCAL folder, open a terminal and enter the following commands:
- `pip install pipenv`
- `pipenv shell` create a pipenv environement to 
- `pipenv install` install all required modules
- create a .env file
- copy the content of .env.sample in the .env file and modify the url_database and the secret_key 

#### configure database for the first time:
- sqlite3: inside sucal folder, open python in a terminal and enter the following commands:

`from app import db, create_app `

`db.create_all(app=create_app()) `

- postgresql 12: Create the database with the name sucal and change the url in the .env file to : "postgresql://postgres:PASSWORD@localhost:5432/sucal"

Don't forget to replace PASSWORD with your postgres password

## This website is not made by, affiliated with or endorsed by Sorbonne Université
- the only official thing here is:  the 'calendar data' extracted from the officiel website



#### credits:
- Louis pour son aide
- Calendar vector created by freepik
