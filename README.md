# Find a Gardener
## Introduction
Find a gardener is an application built in django using python with html and css. It allows users to find local garden companies or customers which require particular
services. Targeting both business' and customers, it allows users to select various services that they offer, or need and target certain cities in order to find someone
who is available to help them. 
![Home Screen]()
![To view the live site please click here](https://find-a-gardener.herokuapp.com/)
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
  - Userbility navigating the site.
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
image image image image
 ### Design
   - When Creating this application I found that an abundance of pre-built templates fit the mold of what I was trying to achieve, I eventually settled on a 
        template that fit the asthetic that I was trying to achieve, although I customised the contents of the template the basic structure is from a template.
        TEMPLATE SOURCE ![link to template source](https://startbootstrap.com/theme/one-page-wonder)
 ### Images
   - I felt that although the theme throughout the site is quite bright and colourful that I should use images that would bring back to the angle the 
     site is coming from, with gardening and horticulte being prominent. Images sourced from ![Unsplash.com](https://unsplash.com/)
## Features
  ### Home Page
  A vibrant homepage was created to welcome users to the site and create intrigue and excitement. Below the main banner style head of the page is a section containing
  information relavent to the site including reviews from previous users.
  An important feature of the homepage is the Locations section, this allows potential users to see where the application is currently active, although still encouraging them to sign up for the future, the list of cities is updated as more users create accounts in cities that might not appear on the list when they sign up
  but will do after they key in there location.
  image image image
  ### Navigation Bar
  A functional yet discreet navigation bar was created in order to not detract away from the main content. When a user is authenticated their options within the nav bar will change to more functional options, 'matches','update profile' and 'logout' whereas someone who is yet to log in will only see, 'home','sign-up','log-in'.
  image image image
  ### Sign-Up
  This section utilises the allauth sign up form, combined with custom form inputs created in order to allow the user to create a full user profile containing the 
  neccesary information to perform the searches.
  image image image
  ### Matches
  The matches page, is loaded from when the user signs up, this page automatically displays the results from a function that searches the database based on the users 
  requirements and returns them to the user in a carousel, this display allows the user to see the individual users individually. When the user hovers over the user they may be interested in the carousel stops, the carousel can also be rotated by the use of the key board keys (<- and ->). The matches page will also display after the user has updated their profile allowing the user to see how their reselected options will effect their search.
  image image image
  ### Profile Update
  The profile update page is easily accesible to the user, always located in the navigation bar once the user is logged in, it provides the user a chance to change search options, this could be to change the services they require/offer or to change their location the user can also change their email in this section. 
  image image image
  ### Admin
  In order to fully utilies the allauth authentication with a custom model, it was neccesary to edit the AUTH_USER_MODEL to include the extra features I wanted to add to the User model, this was created in the admin.py file creating and adapting the 'search fields'.
  image image image
 ## Future Goals
   - As a user I would like to upload my own profile image in order to give my profile more personality.
   - As a site owner I would like to implement an email function, allowing users to email customers or businesses directly from the application(django.mail, or django.postman)
   - As a user/site owner, I would like to be able to tailor my search results based on distance. (i.e 'within 10 miles of my locations) this could be achieved by using django.locations.
   - The implemtation of a description area for users profiles, to include the information about themselves and maybe their website etc.
 ## Testing
 ### Testing Implementation Strategy
 When testing this site I found that testing it manually as a user would prove to be the most effect method for the application in its current stage.
 
 #### Testing Goals
 Testing was ordered into sections of how a user would process through the site, I started to implement these tests as soon as it was feesibly possible in order 
 to allow me to fix issues during development instead of backtracking and potentially causing more issues as development went on.
 
 #### Validator Testing
 All code has been validated using the appropriate validators. All code passed validation.
 
 
      
      




