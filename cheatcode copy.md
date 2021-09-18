creating venv
```py
    py -m venv ./venv
```


activate the venv file. mac is din and window is Scripts

```py
    source ./venv/Scripts/activate
```


to deativate the venv

```py
    deactivate
```


creating a django project [name] is the name of project and [location] if you wanna create in current location, just use .

```py
    django-admin startproject [name] [location]
```


checking all the libraries ar packaged that are installed in this venv

```py
    pip freeze
```


creating an django appliaction inside django project. [name] is name of the app.

```py
    django-admin startapp [name]
```

running the django project

```py
    py manage.py runserver
```

if py cant run server then download django

```py
    pip install django
```

We are going to use [from django.shortcuts import render] only when we have [jinja] template otherwise, we will use [from django, http import HttpResponse] to return raw [html]

```py
    from django.shortcuts import render
    from django.http import HttpResponse

    def index(request):
        html = "<h1>Hello world</h1>"
        return HttpResponse(html)

```

migrate

```py
    py manage.py migrate
```

create SuperUser

```py
    py manage.py createsuperuser
```



```py
py manage.py makemigrations
```



```py
py manage.py migrate
```
### db commands
list of database

```py
\l
```

see my username

```py
\du
```

create database

```py
CREATE DATABASE [name] OWNER [username];
```

### after making database
go into your settings.py and change the database like this.

```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'btredb',
        'USER': 'postgres',
        'PASSWORD': 'dragonpdwer1-',
        'HOST': 'localhost',
    }
}
```


```py
pip install psycopg2-binary
```