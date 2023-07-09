Django-Script automates the setup and configuration of Django applications. This streamlines the development process, allowing developers to focus on building application features.

## Initial Commands



 **startproject**

```
  django-script startproject <project_name>

```
It is the initial setup process for creating a new Django project, allowing you to quickly get started with development.

 **startapp**
```
  django-script startapp <app_name>
```
It is used to create a new Django application within an existing Django project.

**Features**
- Automatically add app name to installed apps in settings.py
- If your current directory has only a Django project, you can use commands even if you are outside the project directory.



## Static Command

```
  django-script addstatic

```
This command creates all the default folders for frontend in Django.

**Features**
- Generates template, static, and media folders.
- Adds configurations to settings.py and urls.py.

## React Command
```
  django-script addreact

```
This command setup Django project with rest framework.

**Features**
- Add django restframework and corsheaders configurations
- Generate React folder and install all necessary basic packages with django. **(In development)**


## Scheduler Command
```
  django-script addscheduler

```
This command sets up Django for executing scheduled jobs in the background automatically.

**Features**

- Adds Django APScheduler configurations to settings.py.
- Creates the project with a job store for execution of tasks.
- Generates scheduler.py and Job.py.
- Detailed code explanation for [**scheduler**](https://github.com/santhoshparthiban2002/Django-scheduler)

## Multi User Command
```
  django-script addmultiuser userType1 userType2 userType3

```
This command sets up Django with a multiuser service.

**Features**

- Sets up Django multiuser data models.
- Allows you to create an unlimited number of different categories of users, such as students, teachers, employees, etc.
- Automatically migrates the data models to the database.