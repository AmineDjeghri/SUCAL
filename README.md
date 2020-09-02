# SUCAL
Sorbonne Université calendar (unofficial)

[![Build Status](https://travis-ci.com/AmineDjeghri/SUCAL.svg?branch=master)](https://travis-ci.com/AmineDjeghri/SUCAL)
<p align="center">
  <img src="images/sucal_logo_500.png">
</p>

# Features
- a fast website that loads your calendar in less than second compared to more than 25sec on the official website
- mobile responsive & better design
- calendar updated every 30min


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

- postgresql 12: Create the database with the name sucal and change the url in the .env file to : "postgresql://postgres:PASSWORD@localhost:5432/sucal" & Don't forget to replace PASSWORD with your postgres password

#### TO DO:
- account authentification to save your calendar 
- receive a notification to tell you 10min before a course where it is
- utc timzone parsing (see if it is 100% correct)
- handle error pages like 404 when a user try to enter a master URL that does not exist

## This website is not made by, affiliated with or endorsed by Sorbonne Université
- the only official thing here is:  the 'calendar data' extracted from the officiel website

## Hosting:
- Heroku
- cron-jobs.com for schedual pinging and 30min updates

#### credits:
- Louis pour son aide
- Calendar vector created by freepik modified by me