# django_account
boilerpalte code for a customUser django app

### this is designed to work with django and django-allauth

#### this is a basic code, nothing special
#### be sure to check the setings and change things to fit your project

#### there is an extra view that i added to the accounts app, it extends a basic django view to add a page for after logging out is complete

#### settings has set your base page as 'home', you migt want to change it at `LOGIN_REDIRECT_URL`

#### this project is used to use email instead of username for logging in


#### the custom user has no extra stuff, it just paves the road for forthur improvment, <a href="https://github.com/cookiecutter/cookiecutter-django/blob/master/%7B%7Bcookiecutter.project_slug%7D%7D/%7B%7Bcookiecutter.project_slug%7D%7D/users/models.py">cookiecutter-django</a>has an example for this

#### the templates are mainly placeholders so you know what each template should be named, no real content. although <a href="https://github.com/pennersr/django-allauth/tree/main/allauth/templates/account">django-allauth</a> has more templates you can use

#### thanks to <a href="https://github.com/wsvincent/awesome-django">william vincent</a> and everyone else who has a guide on this 
