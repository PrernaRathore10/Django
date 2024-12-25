# Django

## How to start project ?

**Django Overview** :

* Django is a mature and rapid development framework.
* Avoid comparing it to JavaScript frameworks; closer comparisons can be made to Laravel or Ruby on Rails.

**Virtual Environment Setup** :

* Virtual environments isolate dependencies and prevent conflicts.

1. *Commands for creating virtual environments*:

* Use `python -m venv <env_name>` or tools like `venv`, `pip`, and `pipx`.
* Activation:
  * On Mac/Linux: `source <env_name>/bin/activate`
  * On Windows: `source <env_name>\Scripts\activate`

2. *Installation Process* :

* Install Django using `pip install django`.
* Use `pip` commands within the virtual environment to ensure proper package management.

### Creating, Updating, and Installing `requirements.txt` File

This helps ensure your project’s dependencies are easily shared and installed across environments.

1. *Creating:*
   - Generate: `pip freeze > requirements.txt`

2. *Updating:*
   - After installing new packages, update: `pip freeze > requirements.txt`

3. *Installing:*
   - To install all dependencies from `requirements.txt`: `pip install -r requirements.txt`

**Advantages of Django** :

* Scalable and efficient even on minimal system resources.
* Popular among corporations for reducing infrastructure costs.
* Secure by default, protecting against common vulnerabilities.

---
## Flow of request

![screenshot](Images/Screenshot%202024-12-24%20134542.jpg)

---
## Levels of Django

![screenshot](Images/Screenshot%202024-12-24%20154859.jpg)

---

## Starting a New Django Project

1. Create project: `django-admin startproject <project_name>`
2. Navigate: `cd <project_name>`
3. Run server: `python manage.py runserver`

---

## Running an App

1. Create app: `python manage.py startapp <app_name>`
2. Register in `settings.py` under `INSTALLED_APPS`

---

## Additional Commands

1. Migrate DB: `python manage.py migrate`
2. Create superuser: `python manage.py createsuperuser`
3. Run tests: `python manage.py test`

---

# **Django Essentials**

---

## **1. `urls.py`**
- Maps URLs to their respective views.
- Contains `urlpatterns` list, which routes user requests.
- Use `path()` or `re_path()` for routing:
  ```python
  from django.urls import path
  from . import views

  urlpatterns = [
      path('', views.home, name='home'),
  ]
  ```
- Important: Include app-level URLs in project-level `urls.py`:
  ```python
  from django.urls import include
  urlpatterns = [
      path('app/', include('app.urls')),
  ]
  ```

---

## **2. `views.py`**
- Contains Python functions/classes that handle requests and return responses.
- Common types of views:
  - **Function-based views (FBV):**
    ```python
    from django.http import HttpResponse

    def home(request):
        return HttpResponse("Hello, World!")
    ```
  - **Class-based views (CBV):**
    ```python
    from django.views import View
    from django.http import HttpResponse

    class HomeView(View):
        def get(self, request):
            return HttpResponse("Hello, World!")
    ```
- Can render templates using `render()`:
  ```python
  from django.shortcuts import render

  def home(request):
      return render(request, 'home.html')
  ```

---

## **3. Templates**
- HTML files used to render data dynamically.
- Stored in the `templates/` folder within apps or at the project level.
- Use Django Template Language (DTL) for dynamic content:
  ```html
  <h1>Welcome, {{ user.name }}</h1>
  ```
- Configure template directory in `settings.py`:
  ```python
  TEMPLATES = [
      {
          'BACKEND': 'django.template.backends.django.DjangoTemplates',
          'DIRS': [BASE_DIR / 'templates'],
      },
  ]
  ```

---

## **4. Static Files**
- Includes CSS, JS, images, etc.
- Stored in the `static/` folder within apps or at the project level.
- Define static files in `settings.py`:
  ```python
  STATIC_URL = '/static/'
  STATICFILES_DIRS = [BASE_DIR / 'static']
  ```
- Use `{% static %}` tag in templates:
  ```html
  <link rel="stylesheet" href="{% static 'css/style.css' %}">
  ```

---

## **5. Important Settings**
- **Base Directory**:
  ```python
  import os
  BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
  ```
- **Debug Mode** (for development):
  ```python
  DEBUG = True
  ```
- **Allowed Hosts** (for production):
  ```python
  ALLOWED_HOSTS = ['localhost', 'yourdomain.com']
  ```
- **Database Configuration**:
  ```python
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.sqlite3',
          'NAME': BASE_DIR / 'db.sqlite3',
      }
  }
  ```
- **Static Files & Media Files**:
  ```python
  STATIC_URL = '/static/'
  MEDIA_URL = '/media/'
  MEDIA_ROOT = BASE_DIR / 'media'
  ```

