# Recipes-Connected | Taste the World at Home
Recipes-Connected is a website for foodies. Users can learn how to cook different recipes from all over the world. Each user can add, edit, and delete their recipes by creating a registration and logging into their profile. Each recipe contains an ingredient list, cooking instructions and an image of the dish. The goal of the website is to have users share and/or learn recipes from all over the world. The website should give the user an ‘learning’ experience.

![alt text][logo]

[logo]: https://raw.githubusercontent.com/MatthewYong/recipes-connected/master/static/images/readme-images/image-landing-device.png

## Table of Contents
- [UX](#ux)
  * [Strategy Plane](#strategy-plane)
  * [Scope Plane](#scope-plane)
  * [Structure Plane](#structure-plane)
  * [Skeleton Plane](#skeleton-plane)
  * [Surface Plane](#surface-plane)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)
- [Disclaimer](#disclaimer)


## UX
To understand what the end result of the website needs to be, we need to define the development process of each stage. This can be done by analysing and breaking down the problem into five planes:

### Strategy Plane
The strategy plane defines the developer’s objective and the user needs (goals).

#### User Stories
As a **user** I want to:
1.  Learn new recipes
2.	Contact the recipe owner
3.	Add my own recipes
4.	Edit my recipes
5.	Delete my recipes
6.	Register my profile
7.	Login to my profile

As a **developer** I want to:
1.  Gain more knowledge on Python, MongoDB and Flask
2.  Learn more on databases, in particular MongoDB
3.  Add and share my own personal favorite recipes on the website

### Scope Plane
The scope plane defines the features that are and are not possible to include on the website.
This will be further explained in the next chapter. A summary of the included and not included features are:

| Features (included) | Future features (not included)|
| :------------- | :---------- |
|1. Navigation menu | 1. Contact form to contact the owner of the recipe|
|2. Hero image with link to add recipes | 2. Rearranging the recipes by name|
|3. Landing page with category recipes| 3. Rating a recipe
|4. Add recipe page | 4. Adding a comment to a recipe
|5. Edit recipe page |
|6. Registration page |
|7. Login page |
|8. User's profile page |

### Structure Plane

The structure plane defines the information architecture and interaction design with the user. The following definitions has been used for this website:

- First impression of the website needs to be simple and clear as possible
- No more than three clicks are required for the user to reach the page
- The type of information architecture that will be used is the ‘Hierarchical Tree’, see below:

![alt text][wireframe tree]

[wireframe tree]: https://raw.githubusercontent.com/MatthewYong/recipes-connected/master/static/images/readme-images/image-wireframe-structureplane.jpg


### Skeleton Plane
The skeleton plane defines a basic visual design of the website through, for example, a wireframe.  
The wireframes for this project are made with Balsamiq can be downloaded from the following link:

- [Wireframe - Desktop version](https://github.com/MatthewYong/recipes-connected/raw/master/static/wireframes/Wireframe%20-%20Desktop.pdf)
- [Wireframe - Tablet version](https://github.com/MatthewYong/recipes-connected/raw/master/static/wireframes/Wireframe%20-%20Tablet.pdf)
- [Wireframe - Mobile version](https://github.com/MatthewYong/recipes-connected/raw/master/static/wireframes/Wireframe%20-%20Mobile.pdf)

Below you can find an example of a wireframe of the landing page.

![alt text][wireframe]

[wireframe]: https://raw.githubusercontent.com/MatthewYong/recipes-connected/master/static/images/readme-images/image-wireframe-skeletonplane.jpg


### Surface Plane
The surface plane defines the appearance of the website. This website needs to attract and encourage users to focus on the website's content.
The following design style has been used:

| Design Style | Design Choice|
| :------------- | :---------- |
Font: Playfair Display | A clear font to give the website a personal look|
Text colour: #152a23 | A dark green color|
Background colour: #fff7| To enhance the recipe images |
Contrast ratio: 9.26 | A high ratio to express the visibility of the text (source: contrast-ratio.com)|


## Features
A summary of the features was described in the scope plane. This chapter will explain what the purpose is of each feature and what will be left to implement for the future.


### Existing Features
| Features (included) | Explanation|
| :------------- | :---------- |
|1. Navigation menu | 1. Allows user to quick access different pages of the website|
|2. Hero image with link to add recipe | 2. Allows users to quick access the add recipe page |
|3. Landing page with category recipes | 3. Allows users to quick access a specific recipe category|
|4. Add recipe page | 4. Allows users to add their recipe by filling out the recipe form|
|5. Edit button/recipe page | 5. Allows users to edit their own recipes|
|6. Login page | 6. Allows users to login to their profile|
|7. Registration page | 7. Allows users to create a new profile
|8. User's profile page | 8. Allows users to view all of their own recipes


### Features Left to Implement
| Features (not included) | Explanation|
| :------------- | :---------- |
|1. Contact form | This feature allows users to contact the owner of a recipe for comments or tips|
|2. Rearranging the recipes by name | This feature allows users to rearrange the recipes by alphabet
|3. Rating a recipe | This feature allows users to give the recipe a rating|


## Technologies Used
The following technologies have been used to achieve this project:

Resources
- [HTML](https://www.w3.org/TR/html52/) is used as the main writing language of this project
- [CSS](https://www.w3.org/Style/CSS/Overview.en.html) is used for styling the HTML text
- [JavaScript](https://www.javascript.com/) is used for adding button alerts
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/) is used as templating language for Python and its depending framework Flask

Styling
- [FontAwesome](https://fontawesome.com/) is used to improve the visual design of the website
- [Contrast-ratio.com](https://contrast-ratio.com/) is used to test the visibility of the text with the background color
- [Google fonts](https://fonts.google.com/) is used for the style the font

Framework & API
- [Flask](https://flask.palletsprojects.com/en/1.1.x/) is used as main  web framework for the website
- [Bootstrap](https://getbootstrap.com/) is used for its grid system and navigation bar. 

Database & Platform
- [MongoDB](https://www.mongodb.com/) is used for storing data from users. Specifically for this website: storing of user information and user recipes.
- [Heroku](https://heroku.com/) is used for deploying the app through the its cloud platform

Images
- [Adobe Photoshop CC 2019](https://www.adobe.com/uk/products/photoshop) is used to crop the images and delete white background
- [Tinyjpg.com](https://tinyjpg.com/) is used to reduce the size of the JPG images
- [Tinypng.com](https://tinypng.com/) is used to reduce the size of the PNG images


Wireframe
- [Balsamic](https://balsamiq.com/) is used to draw wireframes for the skeleton plane and making the visual design of the structure plane

Testing
- [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) is used to test the responsiveness of the website and to debug any problems
- [Unicorn Revealer](https://chrome.google.com/webstore/detail/unicorn-revealer/lmlkphhdlngaicolpmaakfmhplagoaln?hl=en-GB) is used to determine any overflow on the website
- [Validator.w3.org](https://validator.w3.org/) is used to validate the HTML code
- [Jigsaw.w3.org/css-validator](https://jigsaw.w3.org/css-validator/validator.html.en) is used to validate the CSS code
- [JSHint](https://jshint.com/) is used to validate the JavaScript code

## Testing


## Deployment

### Requirements
- Python (minimal version 3.0)
- Heroku account
- Github account

### Cloning the Repository
To work with a local copy of this project the following steps needs to be taken:

#### Step 1: Cloning a local copy
1. Go to the main page of the GitHub repository and click on the dropdown menu 'Code'
2. Copy the URL and go to your local IDE (Integrated Development Environment)
3. In the terminal of your IDE type in 'git clone' and the paste the URL copied from step 2
4. Press Enter and the clone will be created

#### Step 2: Setting up the requirements




### Heroku Deployment
To host this project on Heroku the following steps needs to be taken:











## Credits
### Content
- All text in the website is written by myself, except for the recipes which are taken from [BBCgoodfood](https://bbcgoodfood.com)
- To maintain consistency through all my Code Institute projects, a similar structure for the readme file has been used from my previous projects

### Media
- All photos for this project are used from:
    - [Unsplash.com](https://unsplash.com)
    - [BBCgoodfood.com](https://bbcgoodfood.com)


### Source of codes
The following codes were inspired or taken from:
- [Code Institute](https://codeinstitute.net/) For guidance throughout this project based on the Flask mini project in module Datacentric development
- [Python Programming](https://pythonprogramming.net/decorator-wrappers-flask-tutorial-login-required/): How to use decorators in Flask. Code used on line 31 in app.py
- [Zetcode](http://zetcode.com/python/bcrypt/): How to use bcrypt to hash password in Python. Code used on line 154 in app.py
- [YouTube](https://www.youtube.com/watch?v=vVx1737auSE): How to create login system using Python, Flask and MongoDB. Code used on line 186 in app.py


### Acknowledgement
The completion of this project could not have been possible without support and the extensive knowledge of other people. My appreciation goes to:
- Gerard (Gerry) McBride, my mentor, for giving me tips on how to start with coding in Python, how to use bcrypt for encrypting password, guidance throughout the project and giving me useful tips to finish a good project
- Code Institute, for the valuable lessons through videos and exercises
- Stack Overflow, for giving me code support 
- Slack community for giving me new ideas and code support and helping me deploy my app on Heroku

## Disclaimer
This website is for educational purposes only. All content and images are illustrative.
