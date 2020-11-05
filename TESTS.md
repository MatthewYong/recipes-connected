# Recipes-Connected | Testing


## Table of Contents
- [Manual Testing](#manual-testing)
    * [Navigation Testing](#navigation-testing)
    * [Browser and Mobile Devices Testing](#browser-and-mobile-devices-testing)
- [Key Issues and Code Validation](#key-issues-and-code-validation)


## Manual Testing
Manual tests have been done throughout the development of the project.  
The following test scenarios confirms that the website is behaving accordingly, and that bugs have been taken care of:

### Navigation Testing
#### Access each Category Page through Landing Page
1. On the landing page click on a category
2. Verified that this will open the target page
3. Go back to the landing page and click on the remaining categories
4. Verified that each page with the related category will open

#### Access each a Recipe Page through All Recipes Page
1. On the All Recipes page click on a recipe
2. Verified that this will open the target page

#### Access each Element on the Navigation menu
1. On any page click on one of the elements in the navigation menu
2. Verified that this will open the target page
3. Repeated step 1 and 2 for remaining elements

#### Access each Element on the Footer
1. On any page click on one of the social media icons in the footer
2. Verified that this will open the target page
3. Repeated step 1 and 2 for remaining icons


### Feature Testing
#### Add Your Recipe Button
1. Login into account
2. Click on button **Add Your Recipe**
3. Verified that this will open the Add Recipe page
4. Logout of an account
5. Click on button **Add Your Recipe**
6. Verified that this will open the Login page
7. Verified that the text message **'Please Login First!'** will appear below the password input

#### User Profile - My Recipes
1. Login to account
2. Add a recipe
3. Go to the My Recipes page
4. Verified that the added recipe is shown on My Recipes page

#### Add Recipe
1. On Add Recipe page:
    - Fill in the form,
    - Add a valid image
    - Select a category and a preparation time from the dropdown menu
2. Click on button **Add!**
3. Verified that that a window will pop up with the text **'Recipe is Added!'**
4. Verified in All Recipes page that the recipe has been added
5. Verified that the added recipe exists in the related category

#### Edit Recipe
1. Add a recipe and go to the added recipe page
2. Click on button **Edit**
3. Make changes to the form
4. Click on button **Update**
5. Verified that that a window will pop up with the text **'Recipe is Updated!'**
6. Verified that the recipe is updated

#### Delete Recipe
1. Add a recipe and go to the added recipe page
2. Click on button **Delete**
3. Verified that that a window will pop up with the text **'Recipe is Deleted!'**
4. Verified that the recipe is deleted in all recipes page
5. Verified that the added recipe deleted in the related category

#### Registration - Successful
1. Click on **Register** button in navigation menu
2. Choose an email, username and password
3. Click on **Register** button of the form
4. Verified that profile has been created and redirected to landing page

#### Registration - Unsuccessful
1. Click on **Register** button in navigation menu
2. Choose an existing email
3. Verified that registration failed and that a text message **'The email address already exist'** will appear under the password input 
4. Choose an existing username
5. Verified that registration failed and that a text message **'The username already exist'** will appear under the password input 

#### Login - Successful
1. Click on **Login** button in navigation menu
2. Fill in your username and password
3. Verified that login was succesful and redirected to landing page

#### Login - Unsuccessful
1. Click on **Login** button in navigation menu
2. Fill in your a wrong username and/or password
3. Verified that login failed and that a text message **'Invalid username/password'** will appear under the password input 

#### Logout
1. Login into account
2. Click on logout button in navigation menu
3. Verified that this will open the login page 
4. Verified that a text message **'Logout Successful!'** will appear under the password input
5. Verified that Add Recipe, My Recipes, Logout button disappears from the navigation menu

#### 404 Error Testing
1. Open any page on the website
2. Add extra text to the address bar to change the URL
3. Verified that link does not exist and 404 page will show

#### 404 Category Error Testing
1. Open a category page
2. Add extra text to the address bar to change the URL
3. Verified that category does not exist and 404 page will show


### Browser and Mobile Devices Testing
All the test scenarios have been carried out in the browsers and mobile devices as listed below. No problems were found regarding the responsiveness, overflow and the functionality.

#### Browser Testing
- Google Chrome - version 86.0.4240.111 (64-bit)
- Mozilla Firefox - version 81.0.2 (64-bit)
- Microsoft Edge - version 86.0.622.63 (64-bit)
- Internet Explorer - version 11.719.18362.0

#### Mobile Device Testing through Chrome DevTools
- Moto G4 
- Galaxy S5
- iPhone 5/SE/6/7/8/Plus
- iPad (Pro)


## Key Issues and Code Validation
### W3C Markup Validator
- No errors or warnings were found on base.html, index.html, add_recipe.html, all_recipes.html, category_recipes.html, edit_recipe.html, get_recipe.html, login.html, register.html, user_recipe.html, 500.html and 404.html

### W3C CSS Validator
- No manual coded related errors or warnings were found on style.css, index.css, recipe.css, loginregister.css and error.css
- Errors and warnings that were found are related to Bootstrap and can be ignored

### JSHint Validator
- No errors or warnings were found on recipe.js

### Pep8 Online Validator
- No errors were found on app.py
- Two warning were found with a message that indicates that the **'line is too long'**. The warning won't affect the application and can be ignored

### Browser and Mobile testing
- No issues were found on Google Chrome, Mozilla Firefox, Microsoft Edge and Internet Explorer
- No issues were found on any mobile devices