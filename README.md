# notes


## Simple Getting Started

used system level django to create project

django-admin startproject password_generator

Then rename the root directory to password_generator_project

Then inside create and app. To do this run either 

django-admin startapp generator
or 
python manage.py startapp generator

Now in password_generator settings.py add the app to the list

Whenever anyone tries to access and endpoint /hello for example
django looks in urls.py 

You then need to create a view in views.py and then link that up with a url
in urls.py import the view

from generator import views

in the generator app views.py 

if needed import httpresponse and use to display text
def home(request):
    return .....

if you then hit localhost:8000/ you should get your text  

Do this 10x and get really used to it!

===================================================================

Templates

create a template dir with the name of the app dir inside so you can tell later

mkdir -p myapp/templates/myapp

drop templates in there

in the views.py file you would need something like this
def home(request):
    return render(request, 'generator/home.html')

Now the home page is changed

So views.py is like my app.py in flask


