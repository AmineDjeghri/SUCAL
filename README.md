# SUCAL : Sorbonne Université calendar
### Le lien: [sucal.aminedjeghri.tk](http://sucal.aminedjeghri.tk/)

[![Build Status](https://travis-ci.com/AmineDjeghri/SUCAL.svg?branch=master)](https://travis-ci.com/AmineDjeghri/SUCAL)
<p align="center">
  <img src="images/sucal_logo_500.png">
</p>

# Sceenshots
Dark Mode          |  Light Mode
:-------------------------:|:-------------------------:
<img src="images/sucal2.png">  |  <img src="images/sucal4.png">
<img src="images/sucal1.png">  |  <img src="images/sucal3.png">

# Features
- A fast website that loads your calendar in less than a second compared to more than 25sec on the official website
- A friendly mobile website
- Dark mode
- The Calendar is updated every 30min
- When you select a special field it will automatically add the events from the general field (ex: you select M1_DAC, the calendar will contain M1_DAC + M1 events)

# Want to contribute ?

# Installation
#### I use pipenv
Inside the SUCAL folder, open a terminal and enter the following commands:
- `pip install pipenv`
- `pipenv shell` create a pipenv environement 
- `pipenv install` install all required modules
- Change the name of the **.env.sample** file to **.env**  

#### Running the project
You need to run these commands everytime you want to run the application:
- `pipenv shell` to activate your project environement
- `flask run` tu start the application
- (optional): each time modifying the database requires to do:
- `flask db migrate -m "Updated the database structure"`
- `flask db upgrade`
  
#### configure database for the first time:
- Install Postgresql 12
- Create the database with the name sucal
- In the **.env** file change the *DATABASE_URL* to : **postgresql://postgres:PASSWORD@localhost:5432/sucal** 
- Don't forget to replace PASSWORD with your postgres password

### TO DO:
- Profile calendars
- Receive a notification to tell you 10min before a course where it is situated
- UTC timzone parsing (see if it is 100% correct)
- Handle error pages like 404 when a user try to enter a master URL that does not exist

## This website is not made by, affiliated with or endorsed by Sorbonne Université
- The only official thing here is:  the 'calendar data' extracted from the official  DevCAl  website

## Hosting:
- Heroku
- cron-job.org for 30min schedual pinging 

#### credits:
- Louis for the idea
- The logo of the app was created by freepik and modified by me
