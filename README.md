# SUCAL : Sorbonne Université calendar
### Le lien: [sucal.aminedjeghri.tk](http://sucal.aminedjeghri.tk/)

[![Build Status](https://travis-ci.com/AmineDjeghri/SUCAL.svg?branch=master)](https://travis-ci.com/AmineDjeghri/SUCAL)
<p align="center">
  <img src="images/sucal_logo_500.png">
</p>

# Sceenshots
|Dark Mode          |  Light Mode|
|:-------------------------:|:-------------------------:|
|<img src="images/sucal2.png">  |  <img src="images/sucal4.png">|
|<img src="images/sucal1.png">  |  <img src="images/sucal3.png">|

# Features
- A fast website that loads your calendar in less than a second compared to more than 25sec on the official website
- A friendly mobile website
- Dark mode
- The Calendar is updated every 30min
- When you select a special field it will automatically add the events from the general field (ex: you select M1_DAC, the calendar will contain M1_DAC + M1 events)

# Want to contribute ?

#### 1- Checkout to develop branch and install the requirements (use python 3.7)
`pip install -r requirements.txt`

(If you use pipenv instead of pyenv or conda, you can find the guide [here](https://github.com/AmineDjeghri/SUCAL/tree/master#if-you-use-pyenv))

#### 2- Run the project
- copy `.env.sample` to `.env` (this file contains the settings of the app)
- run `flask run` in the terminal to start the application
##### 2.2 - Pycharm
- for Pycharm users: you can run the __init__.py in debug mode after enabling Live Edit
- take a look at https://www.jetbrains.com/help/pycharm/live-editing.html#ws_live_edit_activate_procedure)
- In edit configurations of the debug session : check FLASK_DEBUG
 
Now if you go to the address, you should see the website, but there is
no database configured yet. Check the next session to configure the database.

#### 3- configure the database for the first time:
- Install Postgresql 12
- Open pgAdmin4 (postgres app), it should open a new tab in the browser 
- Create the database with the name `sucal` (servers -> postgresql -> databases -> right click and create)
- In the **.env** file change the *DATABASE_URL* to : `postgresql://postgres:PASSWORD@localhost:5432/sucal` 
- Don't forget to replace PASSWORD with your postgres password
- Keep pgadmin running in the background
- Run the _upgrade_ command `flask db upgrade`, if you go to pgadmin in sucal -> schemas -> public -> tables, 
  you should see the table user
  
#### If you want to modify the database models:
- Each time the database models change repeat the _migrate_ and _upgrade_ commands.
- Migrate command : `flask db migrate -m "Your comment"`
- Upgrade command : `flask db upgrade`

### TO DO:
- Profile calendars
- Receive a notification to tell you 10min before a course where it is situated
- UTC timzone parsing (see if it is 100% correct)
- Handle error pages like 404 when a user try to enter a master URL that does not exist

## This website is not made by, affiliated with or endorsed by Sorbonne Université
- The only official thing here is:  the 'calendar data' extracted from the official  DevCAl  website

## Hosting:
- Heroku
- cron-job.org for 30min schedual ping

#### credits:
- Louis for the idea
- The logo of the app was created by freepik and modified by me



#### If you use Pyenv: 
#### Installation
Inside the SUCAL folder, open a terminal and enter the following commands:
- `pip install pipenv`
- `pipenv shell` create a pipenv environement 
- `pipenv install` install all required modules
- Change the name of the **.env.sample** file to **.env**

#### Running the project if you use pipenv
You need to run these commands everytime you want to run the application:
- `pipenv shell` to activate your project environement
- `flask run` to start the application
