# Django Setup Guide (Mac & Windows)

## What is Django?

Django is a Python web framework used to build web applications quickly and efficiently.

---

# Prerequisites

Before installing Django, make sure you have:

* Python installed
* pip installed
* Terminal (Mac) or Command Prompt / PowerShell (Windows)

---

# Check Python Installation

## Mac

Open Terminal and run:

```bash
python3 --version
```

## Windows

Open Command Prompt and run:

```bash
python --version
```

Expected output example:

```bash
Python 3.12.0
```

---

# Install pip (If Needed)

## Mac

```bash
python3 -m ensurepip --upgrade
```

## Windows

```bash
python -m ensurepip --upgrade
```

---

# Create a Django Project

## Step 1: Create a Project Folder

### Mac

```bash
mkdir django-project
cd django-project
```

### Windows

```bash
mkdir django-project
cd django-project
```

---

# Step 2: Create Virtual Environment

A virtual environment keeps project dependencies isolated.

## Mac

```bash
python3 -m venv venv
```

## Windows

```bash
python -m venv venv
```

---

# Step 3: Activate Virtual Environment

## Mac

```bash
source venv/bin/activate
```

Expected output:

```bash
(venv)
```

## Windows

```bash
venv\Scripts\activate
```

Expected output:

```bash
(venv)
```

---

# Step 4: Install Django

## Mac

```bash
pip install django
```

## Windows

```bash
pip install django
```

---

# Step 5: Verify Django Installation

```bash
django-admin --version
```

Example output:

```bash
5.2.1
```

---

# Step 6: Create Django Project

```bash
django-admin startproject mysite
```

Move into the project folder:

```bash
cd mysite
```

---

# Step 7: Run Django Server

## Mac

```bash
python3 manage.py runserver
```

## Windows

```bash
python manage.py runserver
```

Expected output:

```bash
Starting development server at http://127.0.0.1:8000/
```

Open browser:

```text
http://127.0.0.1:8000
```

You should see:

```text
The install worked successfully! Congratulations!
```

---

# Example: Create a Django App

Inside the project folder:

## Mac

```bash
python3 manage.py startapp blog
```

## Windows

```bash
python manage.py startapp blog
```

---

# Project Structure Example

```text
mysite/
│
├── manage.py
├── mysite/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── blog/
│   ├── models.py
│   ├── views.py
│   └── admin.py
│
└── venv/
```

---

# Example: Simple Django View

## Step 1: Edit `blog/views.py`

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello Django!")
```

---

## Step 2: Edit `mysite/urls.py`

```python
from django.contrib import admin
from django.urls import path
from blog.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]
```

---

# Run the Server Again

## Mac

```bash
python3 manage.py runserver
```

## Windows

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000
```

Expected output:

```text
Hello Django!
```

---

# Install Additional Packages

Example:

```bash
pip install djangorestframework
```

Save dependencies:

```bash
pip freeze > requirements.txt
```

Install dependencies later:

```bash
pip install -r requirements.txt
```

---

# Deactivate Virtual Environment

When finished working:

```bash
deactivate
```

---

# Common Commands

| Command                             | Description               |
| ----------------------------------- | ------------------------- |
| `python manage.py runserver`        | Run development server    |
| `python manage.py startapp appname` | Create app                |
| `python manage.py migrate`          | Apply database migrations |
| `python manage.py makemigrations`   | Create migration files    |
| `python manage.py createsuperuser`  | Create admin account      |

---

# Common Issues

## pip Not Found

Try:

```bash
python -m pip install django
```

---

## Permission Denied (Mac)

Try:

```bash
sudo pip install django
```

---

## Virtual Environment Not Activating

### Mac

```bash
chmod +x venv/bin/activate
```

### Windows

Run PowerShell as Administrator and execute:

```powershell
Set-ExecutionPolicy RemoteSigned
```

---

# Recommended VS Code Extensions

* Python
* Django
* Pylance

---

# Useful Links

* Django Official Documentation
  https://docs.djangoproject.com/

* Python Official Website
  https://www.python.org/