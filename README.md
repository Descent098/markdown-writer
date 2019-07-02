# Markdown Writer
A simple article writing flask app/microservice. Meant to be accessible on a desktop or mobile device, and allow for easy grab-n-dev building of full apps.

Authored using [Flask-Heroku](https://github.com/WAQSS/Flask-Heroku)

# Features/goals
- Mobile friendly; You shouldn't have to wait til you get home to write something.
- Simple to use & modify; Extensibility is essential, this is a basic implementation and not indented to have all the 'batteries included' approach of something like a full CMS.
- API ingestible; Meant to easily be able to output content to an API that can be ingested by another service. Allows a huge amount of content portability and easier implementation. 
- Database (optional); If you are looking to have a system that outputs markdown or HTML to a database with a few extra fields it should be a one line configuration change to do so.

# Usage

## Local Development
### Requirements
1. Python 3
2. Pip for python 3

### Setup
1. Install dependencies: This can be done running the following command from the root folder:
   ```
   pip3 install -r requirements.txt 
   ```
2. Running: Run the app using the following command from the root folder 
   ```
   python3 routes.py
   ```
3. Begin developing.

## Deployment to Heroku
### Single click deploy
Once you have built out your app and pushed it to github you can deploy it automatically using the button at the bottom of this readme (as long as you kept the app.json file)

### Video Walkthrough
    *comming soon...*
    
# File and folder structure
I have split the explanation into sections to make it easier to understand.

## The Github Part
.gitignore; A preconfigured gitignore file for flask. (info on .gitignore files can be found here: https://www.atlassian.com/git/tutorials/saving-changes/gitignore)

LICENSE; The liscence for the repository, in this case i'm using [MIT](https://choosealicense.com/licenses/mit/)

readme.md; The document you are currently reading, contains all the important info about usage of this repository

---
## The Flask Part
routes.py; Contains all routing information, as well as an important snippet about getting the external port from an environment variable. This portion of the code (found on line 11) is essential to the app working on Heroku.

requirements.txt; Marks all the dependencies necessary to run the app.

### /static
*This is the folder that contains all the HTML CSS and Javascript for the default 'app', the breakdown for the subfolders is found below*

boostrap: This folder contains all the files for bootstrap, a library that allows you to build responsive html apps/websites. Details on the library can be found here: https://getbootstrap.com/

css: This contains all the CSS for the default app, feel free to re-use the folder with your own styles or mess around with the default ones.

fonts: Contains all the font files needed for the icons, and pages of the default app.

img: Contains all the images necesary for the default app.

js: Contains all the javascript (minus bootstrap) necesary for the default app.

templates: Contains all the html files that are routed to from routes.py

manifest.json: Allows the default app to be PWA compliant, more details can be found here: https://developers.google.com/web/fundamentals/web-app-manifest/

---
## The heroku part
Procfile; Where you specify what you want Heroku to run. Keep in mind that only services marked as *web* services have access to external ports.

App.json; Provides some metadata to Heroku, and allows for the single click deploy button found below.

runtime.txt; Allows you to specify a python version that heroku will run your app with.

## Additional info
The app is using [Quill](https://quilljs.com/) as the primay WSYWIG with [higlight.js](https://highlightjs.org/) for the code embedding module. Take a look at both respectively for info on how to configure the editor as you like.

# Single click deploy
Once you have created your own app you can just click here to deploy from your repo

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
