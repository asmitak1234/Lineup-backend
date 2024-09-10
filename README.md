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

   git clone https://github.com/asmitak1234/LineUp-backend.git
   cd lineupbackend
   

2. *Create and Activate a Virtual Environment*

   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   

3. *Install Backend Dependencies*

   pip install -r requirements.txt
   

4. *Configure the Database*

   - Create a MySQL database and user. Update the database settings in [lineupbackend/settings.py](lineupbackend/settings.py):

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

   python manage.py migrate
   

6. *Create a Superuser*

   python manage.py createsuperuser
   

7. *Run the Development Server*

   python manage.py runserver

    The Django Backend development server will typically run on http://127.0.0.1:8000/.
   
Other Requirements are in the file [requirements.txt](requirements.txt)

### Frontend Setup

1. *Navigate to the Frontend Directory*

   cd lineupfrontend
   

2. *Install Frontend Dependencies*

   npm install  # or yarn install
   

3. *Start the Development Server*

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

   ### Overview
      This project involves deploying a Django backend to Vercel, while using AlwaysData for the database. Follow these steps to deploy the application successfully.

   ### Prerequisites

   Before deploying the backend, ensure you have the following:
   
   - Django Project: Ensure your Django project is set up and working locally.
   - Vercel Account: Sign up for a Vercel account if you don't have one.
   - AlwaysData Account: Sign up for an AlwaysData account if you don't have one.
   - Git: Ensure Git is installed and configured on your local machine.

   ### Steps to Deploy

   1. *Setup AlwaysData for the Database*

      Create a Database:

      Log in to your AlwaysData account.
      Go to the “Databases” section and create a new database.
      Note the database name, user, password, and host information.

      Configure Django Settings:

      In your Django project, update the DATABASES settings in settings.py to use the AlwaysData database credentials. Example:

      DATABASES = {
         'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'your_db_name',
            'USER': 'your_db_user',
            'PASSWORD': 'your_db_password',
            'HOST': 'your_db_host',
            'PORT': '3306',
         }
      }

      Install gunicorn and whitenoise and include whitenoise's middleware.
      
      Apply Migrations:

      Run Django migrations to set up the database schema:
      python manage.py migrate

   2. *Deploy Django Backend to Vercel*

      Prepare the Django Project:

      Make sure you have a vercel.json file in the root of your project to configure the Vercel deployment. Example:

      {
         "builds":[
            {
                  "src":"your_project_name/wsgi.py",
                  "use":"@vercel/python",
                  "config":{"maxLambdaSize":"15mb","runtime":"python3.9"}
            }
         ],
         "routes":[
            {
                  "src":"/(.*)",
                  "dest":"your_project_name/wsgi.py"
            }
         ]
      }

      Ensure you have gunicorn in your requirements.txt or Pipfile:
      
      Login to Vercel:

      Login to vercel and click on new project,
      Connect it to github and,
      After pushing all the changes to github ,Select the repository to be deployed
      

      Configure Environment Variables:

      Set environment variables for your Django project in Vercel for deployment and click 'Deploy' button.


   3. *Post-Deployment*

      Collect Static Files:

      Ensure static files are collected for your Django app:

      python manage.py collectstatic --noinput
      
      Check the Deployment:

      Visit the Vercel deployment URL to ensure everything is working correctly.
      Monitor Logs:

      Use Vercel’s dashboard to monitor logs and troubleshoot any issues that arise.






