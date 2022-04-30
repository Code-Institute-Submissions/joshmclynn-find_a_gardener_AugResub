# Find a Gardener
## Introduction
Find a gardener is an application built in django using python with html and css. It allows users to find local garden companies or customers which require particular
services. Targeting both business' and customers, it allows users to select various services that they offer, or need and target certain cities in order to find someone
who is available to help them. 
![Home Screen](https://github.com/joshmclynn/find_a_gardener/blob/main/assets/screenshots/home.PNG)
[To view the live site please click here](https://find-a-gardener.herokuapp.com/)
## Contents
  1. UX(User experience/design)
     - Goals
     - Milestones
     - User Stories
     - Database view
     - Design
     - Images
  2. Features
     - Home Page
     - Navigation Bar
     - Sign-Up
     - Matches
     - Profile update
     - Admin
  3. Future Goals
  4. Technologies Used
  5. Testing
  6. Deployment
  7. Credits 
## User Experience/Design(UX)
  ### Goals
  #### Ideal Users
  - Customers looking for contracters in their local area to carry out works
  - Business's looking to offer their services to customers in their local area.
  - Someone looking for activity regarding horticultural services in certain areas.
  #### Site Goals
  - To provide Business's with a reliable source for their customer base.
  - To provide Customers with a view to business's in the area that could carry out certain works.
  - Usability navigating the site.
  ### Milestones
  At the start of this project I created 5 milestones which were then subdivided in smaller sections within to focus on certain elements within.
  1. Django Project Setup
  2. User Profile
  3. Forms-Database Relations
  4. Search Results
  5. Site Owner objectives
  ### User Stories
  When creating my initial plan of work to be completed I took the five key objectives I had created and then further subdivided them into steps I needed to 
  complete in order to fulfill what I had envisioned when planning this application.
   1. #### Django Project Setup
      - Django Setup, I want to be able to set up Django and install the needed libraries that I have percieved that I will need.
      - Creating and storing keys, I want a secure enviroment to hold secrete keys to avoid exploitation of the application.
      - Deployment to Heroku, I want to be able to deploy to heroku at the earliest possible chance to ensure continues testing and development of the site.
   2. #### Custom User Profiles
      - Create a User account, As a user I want all the information that I provide to be meaningful and relevant information.
      - Users can change profile, As a user I want to be able to change what services I am interested in and the area that I am located.
      - Login/Password, As a user I want my information to be held securely and to have to use login details to gain access to it.
      - Feature Restriction, As a site owner I would like some features to only be accessible for users who are logged in.
   3. #### Form-Database Relationship
      - Meaningful results, As a user I want my information to be processed and stored in a way that will be easily findable for other users.
      - Acknoledgements, As a user I want to know that my information that been processed.
   4. #### Search Results
      - Ease of user, I want a search to be carried out automatically.
      - Meaningful information, As a user I want the information diplayed in the results section be easy to read and hold valuable information.
      - Contact, As a user I want to be able to easily find ways to contact the users displayed in the search
      - Ux , As a user I want to be able to see multiple search results on one page.
   5. #### Site Owner Objectives
      - Responsiveness, As a site owner I want my site to be able to viewed on multiple platforms without a lose of quality or content.
      - Colour Scheme, As a site owner I would like my site to be bright and engaging.
 ### Database View
 I had Created created various options of how I could create the database and models within, In the end I took the decision to utilise allauth connected to a custom
 user model, this allowed me to create users in a singular model allowing for easier querys to the database. Below is the database scheme along side the dataflow for
 application.
![Dataflow](https://github.com/joshmclynn/find_a_gardener/blob/main/assets/screenshots/Dataflow.PNG)
![DataModel](https://github.com/joshmclynn/find_a_gardener/blob/main/assets/screenshots/DataModel.PNG)
 ### Design
   - When Creating this application I found that an abundance of pre-built templates fit the mold of what I was trying to achieve, I eventually settled on a 
        template that fit the asthetic that I was trying to achieve, although I customised the contents of the template the basic structure is from a template.
        [link to template source](https://startbootstrap.com/theme/one-page-wonder)
 ### Images
   - I felt that although the theme throughout the site is quite bright and colourful that I should use images that would bring back to the angle the 
     site is coming from, with gardening and horticulte being prominent. Images sourced from [Unsplash.com](https://unsplash.com/)
## Features
  ### Home Page
  A vibrant homepage was created to welcome users to the site and create intrigue and excitement. Below the main banner style head of the page is a section containing
  information relevent to the site including reviews from previous users.
  An important feature of the homepage is the Locations section, this allows potential users to see where the application is currently active, although still encouraging them to sign up for the future, the list of cities is updated as more users create accounts in cities that might not appear on the list when they sign up
  but will do after they key in there location.
  ![Homepage-Hero](https://github.com/joshmclynn/find_a_gardener/blob/main/assets/screenshots/home.PNG)
  **Key information contained in the homepage below the header section.**
  ![Homepage-Info](https://github.com/joshmclynn/find_a_gardener/blob/main/assets/screenshots/homeinfo.PNG)
  
  ### Navigation Bar
  A functional yet discreet navigation bar was created in order to not detract away from the main content. When a user is authenticated their options within the nav bar will change to more functional options, 'matches', 'update profile' and 'logout' whereas someone who is yet to log in will only see, 'home', 'sign-up', 'log-in'.
  **-Logged In:**
  ![Navigation Bar Logged In](https://github.com/joshmclynn/find_a_gardener/blob/main/assets/screenshots/nav_login.PNG)
  **-Logged Out:**
  ![Navigation Bar Logged Out](https://github.com/joshmclynn/find_a_gardener/blob/main/assets/screenshots/login_nouser.PNG)
  ### Sign-Up
  This section utilises the allauth sign up form, combined with custom form inputs created in order to allow the user to create a full user profile containing the 
  necessary information to perform the searches.
  ![Sign Up Page](https://github.com/joshmclynn/find_a_gardener/blob/main/assets/screenshots/signup.PNG)
  
  ### Matches
  The matches page, is loaded from when the user signs up, this page automatically displays the results from a function that searches the database based on the users 
  requirements and returns them to the user in a carousel, this display allows the user to see the individual users individually. When the user hovers over the user they may be interested in the carousel stops, the carousel can also be rotated by the use of the key board keys (<- and ->). The matches page will also display after the user has updated their profile allowing the user to see how their reselected options will effect their search.
  ![Matches Page](https://github.com/joshmclynn/find_a_gardener/blob/main/assets/screenshots/matches.PNG)
  ### Profile Update
  The profile update page is easily accessible to the user, always located in the navigation bar once the user is logged in, it provides the user a chance to change search options, this could be to change the services they require/offer or to change their location the user can also change their email in this section. 
  Delete profile option is also located in this section, allowing the user to entirely delete their account, this function is only active when the user is logged in.
  ![Profile Edit/Delete](https://github.com/joshmclynn/find_a_gardener/blob/main/assets/screenshots/updateprofile.PNG)
  ### Admin
  In order to fully utilise the allauth authentication with a custom model, it was necessary to edit the AUTH_USER_MODEL to include the extra features I wanted to add to the User model, this was created in the admin.py file creating and adapting the 'search fields'.
  ![Admin site search values](https://github.com/joshmclynn/find_a_gardener/blob/main/assets/screenshots/admin.PNG)
 ## Future Goals
   - As a user I would like to upload my own profile image in order to give my profile more personality.
   - As a site owner I would like to implement an email function, allowing users to email customers or businesses directly from the application(django.mail, or django.postman)
   - As a user/site owner, I would like to be able to tailor my search results based on distance. (i.e 'within 10 miles of my locations) this could be achieved by using django.locations.
   - The implementation of a description area for users profiles, to include the information about themselves and maybe their website etc.
 ## Testing
 ### Testing Implementation Strategy
 When testing this site I found that testing it manually as a user would prove to be the most effect method for the application in its current stage.
 
 #### Testing Goals
 Testing was ordered into sections of how a user would process through the site, I started to implement these tests as soon as it was feasibly possible in order 
 to allow me to fix issues during development instead of backtracking and potentially causing more issues as development went on.
 
 #### Validator Testing
 All code has been validated using the appropriate validators. The code itself was passing the validators a few variables were detected whilst going through the validation process though.
 - The w3 html validator did not seem to like the way the {{for loops}} were written, although I believe this is not an error which I would be able to fix due to the nature of the result from the validator.
![Html Validator Result](https://github.com/joshmclynn/find_a_gardener/blob/main/assets/screenshots/htmlval.PNG)
- VScode picked up a few 'problems' when developing as I have a habit of writing function names in camelCase due to previous experience with java. This was easily rectified.
#### User Testing.

- Sign up form:
      - Goal = Try to break the form
      - Method = Input various random inputs when filling the form in hoping to exploit any shortcomings.
      - Outcome = Due to the form has an amount of validation within the functions I currently have not found a way to exploiting the form.
- Updating Profile:
      - Goal = Try to break the form
      - Method = Input various random inputs when filling the form in hoping to exploit any short comings.
      - Outcome = Due to the form has an amount of validation within the functions I currently have not found a way to exploiting the form.
- User Confusion:
      - Goal = Full cycle of website from sign up to matches.
      - Method = Run through the steps the user would take to sign up to the application
      - Outcome = I found that if the user entered their city they lived in where there was not any matches, the site would not load anything potentially leading to confusion, I decided to solve this by creating pop up messages, in the event that the user has no matches in there area.
- Responsiveness:
      - Goal = Test Responsiveness of the full application.
      - Method = Use Chrome Dev Tools to test responsibility of the site
      - Outcome = Site works on all available options within chrome dev tools, slight overflow on index.html at 320px, I believe that due to increasing phone sizes 320px issues would be negligable.
      
#### Notable Bugs
When trying to implement Javascript into the application I was finding that the Javascript file would not load into the application, I eventually had to move away from using Javascript explicitly in the application due to not being able to find a reason for this. Potential issues with the IDE.
## Technologies Used
- Python
    - The following python modules were used/or plan to be implemented within this project in the future:
        - asgiref==3.4.1
        - asttokens==2.0.5
        - cachetools==4.2.4
        - certifi==2021.10.8
        - cffi==1.15.0
        - charset-normalizer==2.0.8
        - click==8.0.3
        - cloudinary==1.29.0
        - colorama==0.4.4
        - cryptography==36.0.2
        - defusedxml==0.7.1
        - dj-database-url==0.5.0
        - dj3-cloudinary-storage==0.0.6
        - Django==3.2
        - django-allauth==0.50.0
        - django-crispy-forms==1.14.0
        - django-multiselectfield==0.1.12
        - executing==0.8.2
        - Flask==2.0.2
        - google-auth==2.3.3
        - google-auth-oauthlib==0.4.6
        - gspread==5.0.0
        - gunicorn==20.1.0
        - idna==3.3
        - itsdangerous==2.0.1
        - Jinja2==3.0.3
        - jupyter-core==4.9.1
        - MarkupSafe==2.0.1
        - matplotlib-inline==0.1.3
        - mypy-extensions==0.4.3
        - nest-asyncio==1.5.4
        - numpy==1.21.4
        - oauthlib==3.1.1
        - parso==0.8.3
        - pathspec==0.9.0
        - pickleshare==0.7.5
        - platformdirs==2.4.1
        - prompt-toolkit==3.0.24
        - psycopg2==2.9.3
        - pure-eval==0.2.1
        - pyasn1==0.4.8
        - pyasn1-modules==0.2.8
        - pycparser==2.21
        - Pygments==2.11.2
        - PyJWT==2.3.0
        - python-dateutil==2.8.2
        - python3-openid==3.2.0
        - pytz==2021.3
        - pyzmq==22.3.0
        - requests==2.26.0
        - requests-oauthlib==1.3.0
        - rsa==4.8
        - six==1.16.0
        - sqlparse==0.4.2
        - stack-data==0.1.4
        - sweetify==2.3.0
        - tomli==1.2.3
        - tornado==6.1
        - traitlets==5.1.1
        - typing_extensions==4.0.1
        - urllib3==1.26.7
        - wcwidth==0.2.5
        - Werkzeug==2.0.2
- Django
    - Django was used as the main python framework for the development of the project.
    - Django-allauth was used to provide enhanced user account management.
- Heroku
    - Deployment
- Heroku PostgreSQL
    - Used as the database during production and deployment
- Bootstrap
    - Used for layout and spacing requirements and to realise the template I used.
- CSS 
    - Css used from the template, minified to save on storage space.
- Jinja
    - Templating language to insert data into html templates
- HTML 
    - Base language for templates.
- [Sweet alerts2](https://sweetalert2.github.io/)
    - Used for pop up alerts
### Packages Used
- VSCODE
- GITHUB/GITHUB DESKTOP- for storage and version control
- DrawSQL was used to develop database imaging.

### Resources Used
- Django.docs has been used throughout to help during development.
- Stackoverflow, able to research into various ways to perform certain functions etc.

## Deployment
### Project Deployment
To deploy the project through Heroku I followed these steps:

- Sign up / Log in to Heroku
- From the main Heroku Dashboard page select 'New' and then 'Create New App'
- Give the project a name - I entered The-Pantry and select a suitable region, then select create app. The name for the app must be unique.
- This will create the app within Heroku and bring you to the deploy tab. From the submenu at the top, navigate to the resources tab.
- Add the database to the app, in the add-ons section search for 'Heroku Postgres', select the package that appears and add 'Heroku Postgres' as the database
- Navigate to the setting tab, within the config vars section copy the DATABASE_URL to the clipboard for use in the Django configuration.
- Within the django app repository create a new file called env.py - within this file import the os library and set the environment variable for the DATABASE_URL      pasting in the address copied from Heroku. The line should appear as os.environ["DATABASE_URL"]= "Paste the link in here"
- Add a secret key to the app using os.environ["SECRET_KEY"] = "your secret key goes here"
- Add the secret key just created to the Heroku Config Vars as SECRET_KEY for the KEY value and the secret key value you created as the VALUE
- In the settings.py file within the django app, import Path from pathlib, import os and import dj_database_url
- insert the line if os.path.isfile("env.py"): import env
- remove the insecure secret key that django has in the settings file by default and replace it with SECRET_KEY = os.environ.get('SECRET_KEY')
- replace the databases section with DATABASES = { 'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))} ensure the correct indentation for python is used.
- In the terminal migrate the models over to the new database connection
- Navigate in a browser to cloudinary, log in, or create an account and log in.
- From the dashboard - copy the CLOUDINARY_URL to the clipboard
- In the env.py file created earlier - add os.environ["CLOUDINARY_URL"] = "paste in the Url copied to the clipboard here"
- In Heroku, add the CLOUDINARY_URL and value copied to the clipboard to the config vars
- Also add the KEY - DISABLE_COLLECTSTATIC with the Value - 1 to the config vars
 this key value pair must be removed prior to final deployment
- Add the cloudinary libraries to the list of installed apps, the order they are inserted is important, 'cloudinary_storage' goes above 'django.contrib.staitcfiles' and 'cloudinary' goes below it.
- In the Settings.py file - add the STATIC files settings - the url, storage path, directory path, root path, media url and default file storage path.
- Link the file to the templates directory in Heroku TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
- Change the templates directory to TEMPLATES_DIR - 'DIRS': [TEMPLATES_DIR]
- Add Heroku to the ALLOWED_HOSTS list the format will be the app name given in Heroku when creating the app followed by .herokuapp.com
- In your code editor, create three new top level folders, media, static, templates
- Create a new file on the top level directory - Procfile
- Within the Procfile add the code - web: guincorn PROJECT_NAME.wsgi
- In the terminal, add the changed files, commit and push to GitHub
- In Heroku, navigate to the deployment tab and deploy the branch manually - watch the build logs for any errors.
- Heroku will now build the app for you. Once it has completed the build process you will see a 'Your App Was Successfully Deployed' message and a link to the app to visit the live site.

## Credits
- [The original template design](https://startbootstrap.com/theme/one-page-wonder)


 
 
      
      




