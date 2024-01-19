# matriculationCourse
# YOUR PROJECT TITLE
#### Video Demo:  https://youtu.be/N6sytQUjLmU
#### Description: My webpage give to the user math exam to test his skills.
The user first of all must register acount, then sing in and buy course. There is two math courses to buy, basic and advanced. If the user buys a course, the appropriate button will appear in the "your courses" tab. After clicking on the button, user have test to solve. Test have opened and closed examples. After solving user sshould click on the submit button and under this button will show up information with scored points, passed and failed examples.

###### app.py
python main file with backend script, using flask and other libraries.
This file makes registration, signing in, buying, works.
This file checks the correctness of the data that user improved in input field on html file with data stored
This file also checks if the user is logged in and using datebase python check what courses he has.
If user have some course, then this file gives him access to this course.

###### final.db
datebase with information about:
-users including: id, email, name, hashed password
-purchases including: id of purchase, id of user that bought, name of product, date

###### helpers.py
python file with function that help the main file

###### requirements.txt
text file with libraries which are used by python in helpers.py and app.py

##### Static directory
directory wiith static files, including: photoes, images, style sheet files and js script files

###### adva directiory
contains images with 16 math examples on advanced math level

###### bas directory
contains images with 34 math examples on basic (low) math level

###### adult.jpg
photo used to represent the advanced level course on website "buy course" tab

###### back.jpg
photo used to background on every subpage in this website

###### kid.jpg
photo used to represent the low level course on website "buy course" tab

###### favicon.ico
the website icon shown on the top tab in the browser

###### bootstrap.min.css; narrow-jumbotron.css; style.css
files that define the style of the webpage
style.css - mostly defining style on this website. I mean the title of page, navbar, footer, color of text, background, buttons and more.

###### script-ajax.js; script-no-ajax.js
scripts to handle checkout, when the button is pressed this script redirects user to checkout page and in backend, python files start working for a successful purchase.

##### templates directory
directory with html files

###### adv.html
html file with the 16 math examples (containing both, open response and closed response tasks) on advanced math course level,
where user can automaticly check his skills, and see what he passed and failed.

###### apology.html
html file with information when something goes wrong, html file will show that something goes wrong and tell what was that

###### bas.html
html file with the 34 math examples (containing both, open response and closed response tasks) on bassic math course level,
where user can automaticly check his skills, and see what he passed and failed.

###### buy.html
html file with products to buy, in this case, advanced level math course and basic level math course, with photoes and price of courses.

###### courses.html
html file with courses that the user has. The courses that the user has are shown on the buttons with redirection

###### index.html
html file, main page with information about this webpage, button with redirection to buy course and buttons with redirection to social media like facebook, instagram, tiktok

###### layout.html
html file that specifies the apperance of all pages. This file has links to javascript script files, css style sheets, bootstrap.
This file makes the title of website, navbar, footer, and body which uses other files.

###### login.html
html file with login formula. This file has two input field, first to write an email and second of course to write password. Under of input field is submit button.

###### register.html
html file with register formula. This file has four input field, first to write an email, second to write users name, third to write password and fourth to write password again, of course below these fields is the submit button

###### thanks.html
html file that thanks user for buy the course
