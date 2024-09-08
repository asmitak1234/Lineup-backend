<!-- Made by- Asmita Kumari -->

# LineUp-backend
<!-- explaining setup,functionalities, and deployment steps. -->
<!-- ## for heading, # for main heading,following for links and lists ,[CONTRIBUTING.md](CONTRIBUTING.md) file for locating to file.-->


## Description

Hello Everyone, I am ASMITA KUMARI , a young learner and i am here with frontend part of my project called "LineUp" .It is a Task Manager or To-Do List App that helps everyone to manage their daily life tasks with proper details like Title,Description,Created on,Completed or not.This is a simple ,secure and efficient tool to store and order tasks according to their completion status. I am making this project with the intension of helping everyone to not forget the more important tasks they have to do in a day. This project is a React based App with Backend managed with Django (Rest Framework) with MySQL as a Database with proper CRUD(Create,Read,Uodate and Delete) Operations.

This project is a full-stack CRUD(Create, Read, Update, Delete) Web Application using Django for the backend, React for the frontend, and MySQL as the database. This README provides instructions on setting up, using, and deploying the backend of this project.

## Table of Contents

- [Requirements](#requirements)
- [Setup](#setup)
  - [Backend Setup](#backend-setup)
  - [Frontend Setup](#frontend-setup)
- [Connection](#connection)
- [Functionalities](#functionalities)
- [Deployment](#deployment)

## Requirements

- Python 3.8 or higher
- Node.js 14 or higher
- npm (or yarn) for managing JavaScript packages
- MySQL server
- Other Requirements are in the file [requirements.txt](requirements.txt)

## Setup

### Backend Setup

1. *Clone the Repository*

   bash:
   git clone https://github.com/asmitak1234/LineUp-backend.git
   cd lineupbackend
   

2. *Create and Activate a Virtual Environment*

   bash:
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   

3. *Install Backend Dependencies*

   bash:
   pip install -r requirements.txt
   

4. *Configure the Database*

   - Create a MySQL database and user. Update the database settings in [lineupbackend/settings.py](lineupbackend/settings.py):

     python:
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.mysql',
             'NAME': 'your_db_name',
             'USER': 'your_db_user',
             'PASSWORD': 'your_db_password',
             'HOST': 'localhost',
             'PORT': '3306',
         }
     }
     

5. *Apply Migrations*

   bash:
   python manage.py migrate
   

6. *Create a Superuser*

   bash:
   python manage.py createsuperuser
   

7. *Run the Development Server*

   bash:
   python manage.py runserver

    The Django Backend development server will typically run on http://127.0.0.1:8000/.
   
Other Requirements are in the file [requirements.txt](requirements.txt)

### Frontend Setup

1. *Navigate to the Frontend Directory*

   bash:
   cd lineupfrontend
   

2. *Install Frontend Dependencies*

   bash:
   npm install  # or yarn install
   

3. *Start the Development Server*

   bash:
   npm start  # or yarn start
   

   The frontend will typically run on http://localhost:3000.

## Connection 

- *Frontend-Backend*: Frontend and Backend is connected by Axios library.
- *Backend-Database*: Backend and Database is connected through mysqlclient by updating Database information in settings.py after creating database.
 
For Security reasons you can add .env file to protect your sensitive data from settings.py and including it in [.gitignore](.gitignore) file.

## Functionalities

- *User Interface*: A responsive and dynamic user interface built with React.
- *API Integration*: Fetches and posts data to/from the Django backend using RESTful API endpoints.
- *Form Handling*: User input and form submissions are handled with proper validation mechanisms.
- *User Authentication*: Handles user authentication (login, register) through API calls to the Django backend and gives alert to user.
- *Navigation*: Users can navigate to different web pages(Tasks,Login,Logout,Register) through the Buttons on Navigation Bar.
- *CRUD Operations*: Perform create, read, update, and delete operations on the main resources.
- *Details of Tasks*: Details of tasks like Title,Description,Created on,Completion Status is available.
- *Ordering*: Tasks are automatically ordered according to the Completion status.

## Deployment

   #### Overview
      This section describes the steps to deploy the backend of this project, which is built with Django, uses MySQL as its database, and utilizes python-decouple for managing environment variables, to Heroku. The frontend built with React is not covered here but will need to be deployed separately.

   #### Prerequisites

   Before deploying the backend, ensure you have the following:
   
   - A Heroku account (sign up at Heroku).
   - The Heroku CLI installed. You can install it by following Heroku CLI installation instructions.
   - MySQL database and user credentials.
   - Your Django project should be ready for deployment with a requirements.txt file and necessary configurations.

   #### Steps to Deploy

   1. *Prepare Your Django Project*

       - Install Required Packages

         Ensure you have gunicorn, dj-database-url, and python-decouple in your requirements.txt for running the app on Heroku.
         pip install gunicorn dj-database-url python-decouple

         Then, add these to your requirements.txt:
         pip freeze > requirements.txt

         Configure settings.py
         
         from decouple import config, Csv
         import dj_database_url

       - Load environment variables

         SECRET_KEY = config('DJANGO_SECRET_KEY')
         DEBUG = config('DJANGO_DEBUG', default=False, cast=bool)

       - Database configuration

         DATABASES = {
            'default': dj_database_url.parse(config('DATABASE_URL'))
         }

       - Allowed hosts

         ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='*', cast=Csv())
         Create a Procfile
         Create a Procfile in the root directory of your project to tell Heroku how to run your application:

         web: gunicorn myproject.wsgi

         Add Static File Configuration
         Install whitenoise to serve static files:

         pip install whitenoise
         Update your settings.py:
         MIDDLEWARE = [
            'whitenoise.middleware.WhiteNoiseMiddleware',
            # other middleware...
         ]

         STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

         Add whitenoise to requirements.txt:
         pip freeze > requirements.txt

   2. *Deploy to Heroku*

      - Login to Heroku

         Open your terminal and log in to your Heroku account:
         heroku login

         Create a Heroku App
         Create a new app on Heroku:
         heroku create your-app-name

      - Add MySQL Add-on

         Add the ClearDB MySQL add-on (or another MySQL add-on of your choice):
         heroku addons:create cleardb:ignite

         This will provision a MySQL database and provide a DATABASE_URL environment variable.

      - Set Environment Variables

         Configure the environment variables that python-decouple will use. You can dothis through the Heroku CLI or the Heroku Dashboard. Here's how to set environment variables using the Heroku CLI:
         
         heroku config:set DJANGO_SECRET_KEY='your-secret-key'
         heroku config:set DJANGO_DEBUG=False
         heroku config:set ALLOWED_HOSTS='yourdomain.com'
         heroku config:set DATABASE_URL='your-cleardb-database-url'

      - Push Code to Heroku
         Initialize a Git repository if you haven’t already:

         git init
         git add .
         git commit -m "Initial commit"

         Push to Heroku:
         git push heroku master

         Run Migrations:
         heroku run python manage.py migrate

         Create a Superuser (Optional):
         heroku run python manage.py createsuperuser

         Collect static files for production use:
         heroku run python manage.py collectstatic --noinput

   3. *Verify Deployment*

         Once the deployment is complete, open your app in the browser:

         heroku open
         Check that your app is running correctly and verify that all features work as expected.




