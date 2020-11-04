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
#### Access each Category page through landing page
1. On the landing page click on a category
2. Verified that this will open the game page
3. Go back to the landing page and click on the remaining categories
4. Verified that each page with the related cateogry will open




### Browser and Mobile Devices Testing
All the test scenarios have been carried out in the browsers and mobile devices as listed below. No problems were found regarding the responsiveness, overflow and the functionality.

#### Browser Testing
- Google Chrome - version 86.0.4240.111 (64-bit)
- Mozilla Firefox - version 78.0.2 (64-bit)
- Microsoft Edge - version 83.0.478.61 (64-bit)
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
- Two warning were found with a message that indicates that the **'line is too long'**. The warning can be ignored

### Browser and mobile testing
- No issues were found on Google Chrome, Mozilla Firefox, Microsoft Edge and Internet Explorer
- No issues were found on any mobile devices