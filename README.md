# Django ToDo App 🚀
### Experience a simple but powerful ToDo app with user authentication and seamless CRUD functionality.

<p align="center">
  <img src="base\static\images\am-i-responsive.png" alt="Responsive website" width="600">
</p>

[This is the link](https://django-auth-crud-app2-d11a949b5519.herokuapp.com/) to the deployed webpage/URL.

[This is the link](https://github.com/markohautala/django-auth-crud-app) to the GitHub repository for this project.

<hr>

## How to use it

- To be able to use the application you first need to register an account - you will be asked to enter a username and a password.

- When the login is successful, then you are redirected to the "main application". But for a newly created account, there are no tasks created yet. 

- You need to create a task by clicking the button that says "add a task". This will redirect you to a page where you can create a task by giving it a title, description and a check or un-check status. For starters it's maybe relevant that the task is not yet done - so leave it unchecked. 

- After submitting the task, you are redirected back to the task-list where you should see your newly created task. 

- when the task is completed you can edit the task by clicking on the "gear"-icon and edit the task by either adding more info to it or marking it as completed. If you mark it as completed, and re-submit, then you will be redirected back to the task-list and the task is updated with a check-icon, signaling that the task is completed.

- If you wish to delete a task totally that is possible. Just click on the "trash-bin"-icon next to the task you want to delete, and you will be redirected to a confirmation page where you can either click on "delete task" or you can go back to the "main" task page again.



## Features

- All pages should prioritize good UX by ensuring that users never have to rely on the browser's 'back' button to navigate to a previous page. Instead, each page should provide a clearly labeled link for this purpose, contributing to a seamless user experience.

- All the pages have a "home" button that takes the user back to the homepage - except the "delete-task"-page - that page only haves a "go back to task list" button that can take the user back to the full-task-list.

<p align="center">
  <img src="base\static\images\home-button.png" alt="Home button" width="400">
</p>

- The loginpage has input for users that already has registred themself - they can input username and password and after that klick the "login"-button. But incase they have not registrered themselfs as users, they are promted by a text saying "Are you a new user and need to create an account?" and then a button that takes the user to the register-user-page. 

<p align="center">
  <img src="base\static\images\login.png" alt="Home button" width="400">
</p>

- The same as above, but for the register-user-page. There is a form that the user can fill out with username and then a password and a re-type for the password - and of course a button that says "register". But under that form, there is a text promting already created users with the text "Do you already have an account?" and then a login-button that takes the user to the login-page so that the user can login instead.

<p align="center">
  <img src="base\static\images\register.png" alt="Home button" width="400">
</p>

<p align="center">
  <img src="base\static\images\register-2.png" alt="Home button" width="400">
</p>


- When a user has logged-in successfully - then the user is redirected to their task-dashboard. Here they can view all their tasks. 

<p align="center">
  <img src="base\static\images\task-page.png" alt="Home button" width="400">
</p>

- They can click on the button "Add a task" to create a new task which will take the user to the create-task-page. Here the user can create a task by giving the task a title, a description (or not) and then uncheck or check the "completed" check-input. 

<p align="center">
  <img src="base\static\images\create-task.png" alt="Home button" width="400">
</p>

- Once the user clicks on "Create" then the user is re-directed back to the task-list and they can now see their task they just created.

<p align="center">
  <img src="base\static\images\updated-taskpage.png" alt="Home button" width="400">
</p>

- When a user is at the dashboard (task-list), they can also delete and edit the task. To be able to edit a task the user can click on the button next to the task (settings-icon) and then the user is redirected to the task and the form for that specific task. The user can edit any of the field and re-submit/edit the task. They can for example klick on the "completed" check-box and then resubmit and then the user is redirected to the dashboard and now the user can see a "tick"/check next to the task which is giving a visual sensation of completion which is a choise for a good UX. 

<p align="center">
  <img src="base\static\images\complete-task.png" alt="Home button" width="400">
</p>

<p align="center">
  <img src="base\static\images\completed-icon.png" alt="Home button" width="400">
</p>

- The user can also delete tasks by clicking on the "trash-bin-icon" next to the task - this will redirect the user to a confirmation-page where the user is given a question if the user wants to delete the task - if the user clicks on the delete button, then the user is redicted back to the task-list with a succesful deleted task. On the delete-confirmation page, there is also a way for the user to "go back to task-list" incase the user regretted their choise - which is part of good UX aswell.

<p align="center">
  <img src="base\static\images\delete-confirmation.png" alt="Home button" width="400">
</p>

- The user can whenever they want logout from the dashboard which takes the user back to the login-page.

- On the homepage there is text that gives information about the application and also reassures the user that their personal information is secretley and kept private and safe - this gives the user trust for the service and application. Under that section, there is a carousel giving a "high-tech" feeling towards the appliction - the pictures are not of the application itself but just placeholder images that gives a good design and modern feeling towards the webpage/application.

<p align="center">
  <img src="base\static\images\homepage.png" alt="Home button" width="400">
</p>

- Under the bootstrap carousel, there are two cards - one is prompting the user to login if they already have accounts and one is promting the user to create or register an account incase they have not already done that. 

<p align="center">
  <img src="base\static\images\homepage-login-register.png" alt="Home button" width="400">
</p>

- Under this section comes the footer - here is a copyright promt and two icons - one for my personal GitHub nad one for my personal LinkedIn profile.

<p align="center">
  <img src="base\static\images\footer.png" alt="Home button" width="400">
</p>

#### UX design
(UX design with wire frames and database design/schema)

- Database schema: 

| Field         | Type         | Description                                          |
|---------------|--------------|------------------------------------------------------|
| id            | Integer      | Primary key, auto-generated by Django                |
| user_id       | Integer      | Foreign key referencing the User table (nullable)    |
| title         | CharField    | Stores the title of the task                         |
| description   | TextField    | Stores the description of the task (nullable)        |
| complete      | BooleanField | Indicates whether the task is complete or not        |
| created       | DateTimeField| Timestamp of when the task was created               |


#### Future features

- A search function so that the user can search after items after they have created them.

- A due-date, so that the user can prompt a "end date" or "date to finish" the task to.

- A way for a user to be able to delete their whole account - both the account and their created tasks.

- Instead of using a username, the user could be required to enter both their first and last names in the registration form. Then, use the entered first name to greet the user in the tasklist. Currently, the greeting is based on the username, which may not necessarily reflect the user's actual first name. This can be confusing if a user enters a name that is not their first name, and then the page greets them using this potentially unrelated username.

<hr>

## Testing
### Loghthouse Testing
- Performance: 92%
- Accessibility: 100%
- Best Practices: 91%
- SEO: 92%

### Resolved Bugs

#### Bug #1: TemplateDoesNotExist Error

- Description: Under the development environment with DEBUG=True, the Django application raised a TemplateDoesNotExist error for base/task_list.html.
- Solution: Created a templates folder and nested a base folder within it. Added task_list.html inside base with content. Refreshed the browser to confirm resolution, leveraging Django's debug mode (DEBUG) for assistance.

#### Bug #2: TemplateSyntaxError due to Naming Convention

- Description: Declared context_object_name as todo-tasks, causing a TemplateSyntaxError.
- Solution: Renamed todo-tasks to todo_tasks to adhere to Python variable naming conventions, resolving the issue promptly.

#### Bug #3: ImproperlyConfigured Error in ModelFormMixin

- Description: Received an ImproperlyConfigured error on create-task/ due to a typo (fields = '__all__').
- Solution: Corrected the typo to fields = '__all__' in views.py, resolving the error swiftly.

#### Bug #4: CSRF Verification Failure after Form Submission

- Description: Faced a 403 Forbidden error with "CSRF token missing" after submitting a form.
- Solution: Added {% csrf_token %} to the form template. Resubmitted the form, successfully adding the task to the database.

#### Bug #5: TemplateSyntaxError due to Missing URL Template Tag

- Description: Encountered a TemplateSyntaxError related to a missing URL template tag ({% url 'tasks' %}).
- Solution: Corrected the URL template tag by adding {% %} around url, resolving the error promptly.

#### Bug #6: Incorrect Href Path

- Description: Discovered an error due to an incorrect href path when adding a back button.
- Solution: Rectified the href path, resolving the issue and enabling correct page loading.

#### Bug #7: Data Access Control Issue with User Privileges

- Description: Users gained unintended access to all tasks in the database, leading to data privacy and access control issues.
- Solution: Implemented data access controls using get_context_data to restrict task access to authenticated users only, ensuring privacy and control over user-specific tasks.

#### Bug #8: Heroku Application Error (ModuleNotFoundError)

- Description: Encountered a ModuleNotFoundError in Heroku due to a misconfigured directory structure (todo_app.wsgi not found).
- Solution: After extensive debugging and restructuring, resolved the issue by adjusting the directory structure, removing unnecessary nested folders, and redeploying the project on Heroku, successfully resolving the deployment error.

### Unsolved bugs
- So far there are no known unsolved bugs - all bugs tht have been encountered during deployment and production phase have been solved succesfully.

### Validator testing

- CSS: No warnings or problems to show - CSS code validated using W3C CSS Validator and JigSaw.

- HTML: The HTML code passed the W3C validator with no warnings - "Document checking completed. No errors or warnings to show."

- JavaScript: The JavaScript code for this project passed and got validated using the JSHint with no warnings or errors.

- Python code passes Linter with "All clear, no errors found". Python code passes PEP8 without issues.


### Languages and Frameworks
This project was created using the following languages and frameworks:

- Django as the Python web framework.
- Python as the backend programming language.
- HTML as the markup language and templating language.
- CSS as the style sheet language.
- Bootstrap 5 as the CSS framework.
- JavaScript to create footer element that changes
- SQLite to store user data (Relational database)


#### Manual testing write up

<hr>


## Deployment procedure
##### Forking and Cloning the Project
To deploy this Django project, follow these steps to fork and clone the repository:

### Fork the Repository:

- Go to the project's GitHub repository at [this page](https://github.com/markohautala/django-auth-crud-app)

- Click on the Fork button in the upper right corner of the page.

- This will create a copy of the repository under your GitHub account.

### Clone the Forked Repository:

- Go to the GitHub repository https://github.com/markohautala/django-auth-crud-app

- Locate the Code button above the list of files (next to 'Add file') and click it

- choose a preferred cloning option by selecting either HTTPS or GitHub CLI.

- Open Git Bash

- Change the current working directory to the one where you want the cloned directory

- Type git clone and paste the URL from the clipboard ($ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY)

- Press Enter to create your local clone


#### Deploying on Heroku:

1.  **Log in** to the Heroku account.
2.  Navigate to **"New"** and click **"Create new App"**.
3.  Choose a unique **app name** and click **"Create app"**.
4.  Select the preferred **region (e.g., Europe)**.
5.  Go to **"Deploy"** tab.
6.  Click **"Connect to GitHub"**.
7.  Search for the **repository** name in the search field.
8.  Click **"Search"** and then **"Connect"** next to the right repository.
9.  Enable **"Automatic deploys"**.
10.  Click **"Deploy branch"**.

### Setup in the IDE (VS Code):

1.  In the CLI, install **Django-Heroku**: `pip install django-heroku`.
2.  Install **Gunicorn**: `pip install gunicorn`.
3.  Install **Whitenoise**: `pip install whitenoise`.
4.  Create a **"runtime.txt"** file and specify the **Python version** (e.g., `python-3.12.3`).
5.  Create a **Procfile** and add: `web: gunicorn todo_app.wsgi`.
6.  In **settings.py**, add Whitenoise middleware: `MIDDLEWARE=['whitenoise.middleware.WhiteNoiseMiddleware']`.
7.  Also in **settings.py**, set `STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'`.
8.  Add `python-3.12.3` in a **"runtime.txt"** file (Python version used in the project).
9.  In **Procfile**, add logging: `web: gunicorn todo_app.wsgi --log-file -`.
10.  Generate **requirements.txt**: `pip freeze > requirements.txt`.
11.  Import **django\_heroku** and **os** in **settings.py**.
12.  Add the Heroku app's URL to **ALLOWED\_HOSTS**.
13.  Set `DEBUG=False` in **settings.py**.
14.  At the end of **settings.py**, activate Django-Heroku: `django_heroku.settings(locals())`.

* Additional Steps:

*   If the app has static files (JS, CSS), set **config vars** by adding `"DISABLE_COLLECTSTATIC"` with a value of `"1"`.
*   Commit the changes with an appropriate message and **push to GitHub**.
*   **Deploy** the changes on Heroku to apply the new configurations.


<hr>

## Credits
- Comprehensive resource for in-depth understanding of Django class-based views: [ccbv.co.uk](https://ccbv.co.uk/)

- Reference materials aiding comprehension of `get_context_data` in Django: [Django Forum Thread](https://forum.djangoproject.com/t/get-context-data-only-users-data/3904/7)

- Utilized color schemes from [Color Hunt](https://colorhunt.co/) to enhance page aesthetics.

- Leveraged [Heroku Dev Center](https://devcenter.heroku.com/categories/reference) documentation for debugging purposes.

- Incorporated Google Fonts icons from [Google Fonts](https://fonts.google.com/icons) for iconography throughout the application.