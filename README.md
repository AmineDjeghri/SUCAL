# SUCAL
Sorbonne Université calendar (unofficial)

[![Build Status](https://travis-ci.com/AmineDjeghri/SUCAL.svg?branch=master)](https://travis-ci.com/AmineDjeghri/SUCAL)

# Features
- a fast website that loads your calendar in less than second compared to more than 25sec on the official website
- mobile responsive & better design
- account authentification to save your calendar 
- receive a notification to tell you 10min before a course where it is


# Want to contribute ?

# Installation
(brouillon !!!)
#### pipenv 
- shell (create a pipenv environement to install all required module)
- create a .env file
- copy the content of .env.sample in the .env file and modify the url_database and the secret_key 
- create the tables in your database ( give an exemple here for sqlite)
(i will change this later and add a .env file to make the app use sqlite by default with a defaut secret key)

#### configure database
- sqlite3: inside sucal folder, open python in a terminal and enter the follwing commands
`from app import db, create_app `
`db.create_all(app=create_app()) `

-postgresql 12: Create the database with the name sucal and change the url in the .env file to : "postgresql://postgres:PASSWORD@localhost:5432/sucal"

Don't forget to replace PASSWORD with your postgres password

## This website is not made by, affiliated with or endorsed by Sorbonne Université
- the only official thing here is:  the 'calendar data' extracted from the officiel website

Un grand merci à [Louis](https://github.com/lgvld) pour son aide
et 
à ce petit [https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login](tutoriel) 
