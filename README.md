# SUCAL
Sorbonne Université calendar (unofficial)

# Features
- a fast website that loads your calendar in less than second compared to more than 25sec on the official website
- mobile responsive & better design
- account authentification to save your calendar 
- receive a notification to tell you 10min before a course where it is


# Want to contribute ?

# Installation
(brouillon !!!)
- pipenv shell (create a pipenv environement to install all required module)
- create a .env file and modify the url_database and the secret_key and don't forget to create the tables in your database
- for the database 

#### configure database
inside sucal folder, open a python in a terminal 
>>> from app import db, create_app 
>>> db.create_all(app=create_app()) 

## This website is not made by, affiliated with or endorsed by Sorbonne Université
- the only official thing here is:  the 'calendar data' extracted from the officiel website

Un grand merci à [Louis](https://github.com/lgvld) pour son aide
et 
à ce petit [https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login](tutoriel) 
