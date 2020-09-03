# SUCAL
Sorbonne Université calendar 

Le site est disponible [ici](http://sucal.aminedjeghri.tk/)

[![Build Status](https://travis-ci.com/AmineDjeghri/SUCAL.svg?branch=master)](https://travis-ci.com/AmineDjeghri/SUCAL)
<p align="center">
  <img src="images/sucal_logo_500.png">
</p>

# Features
- A fast website that loads your calendar in less than a second compared to more than 25sec on the official website
- A friendly mobile website
- The Calendar is updated every 30min
- When you select a special field it will automatically add the events from the general field (ex: you select M1_DAC, the calendar will contain M1_DAC + M1 events)

# Want to contribute ?

# Installation
(spreadsheet !!!)
#### pipenv or your virtual env
Inside the SUCAL folder, open a terminal and enter the following commands:
- `pip install pipenv`
- `pipenv shell` create a pipenv environement to 
- `pipenv install` install all required modules
- Create a .env file
- Copy the content of .env.sample in the .env file and modify the url_database and the secret_key 

#### configure database for the first time:
- Postgresql 12: Create the database with the name sucal and change the url in the .env file to : "postgresql://postgres:PASSWORD@localhost:5432/sucal" & Don't forget to replace PASSWORD with your postgres password

- Sqlite3: inside sucal folder, open python in a terminal and enter the following commands:

`from app import db, create_app `

`db.create_all(app=create_app()) `

#### TO DO:
- Profile calendars
- Receive a notification to tell you 10min before a course where it is situated
- UTC timzone parsing (see if it is 100% correct)
- Handle error pages like 404 when a user try to enter a master URL that does not exist

## This website is not made by, affiliated with or endorsed by Sorbonne Université
- The only official thing here is:  the 'calendar data' extracted from the official  DevCAl  website

## Hosting:
- Heroku
- Cron-jobs.com for schedual pinging and 30min updates

#### credits:
- Louis for the idea
- Calendar vector created by freepik modified by me