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