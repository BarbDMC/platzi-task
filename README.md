# Platzi-task

It's a to-do list web app that allows creating tasks with a basic login system. It has been made with Python, Flask, and Firebase. It's based on the project from Platzi's course of Flask. 

<br>

## How to start

* Navegate to project's folder
* Create a virtual enviroment with command: `virtualenv venv`
* Activate the enviroment with command: `source venv/bin/activate`
* For deactivate run: `deactivate`
* Install dependencies with: `pip install -r requirements.txt`
* Set flask app running: `set FLASK_APP=main.py`
* For debugging mode: `set FLASK_ENV=development`

<br>

## For use firestore

* Create a [firestore database](https://console.firebase.google.com) with a users collection.
* In firebase console go to: Project settings -> Service accounts -> Firebase Admin SDK.
* Download your crediantials service account selecting *'Generate new private key'*.
* Set GOOGLE_APPLICATION_CREDENTIALS environment variable with the path of your credential json file,<br>
  example: `set GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/service-account-file.json"`

<br>

## Run project

* Use command: `flask run`

<br>

## Run tests

* Use command: `flask test`
