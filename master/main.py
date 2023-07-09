import os
import sys
import subprocess
from .addInstallApp import addApp
from .addHost import addAllHost
from .addMiddleware import addMiddleware
from .addCodeSettings import addCode
from .react import react
from .fileCheck import *
from .multiUser import multiUser
from .scheduler import scheduler
#from .addMail import addMail


def djangoScript():
    callName = sys.argv[1]
    status = 2
    manage_py_path = findCurrentFile('manage.py')
    project_check = findFile('manage.py')
    if manage_py_path:
        status=0
    elif project_check:
        status=1
    elif(callName != "startproject"):
        print("First make the project or go to the project directory")

    if callName == "startproject":
        projectName = sys.argv[2]
        subprocess.run(["django-admin", "startproject", projectName], check=True)
        os.chdir(projectName) 
        addAllHost(projectName)
    
    elif callName == "addreact":
        if (status==0):
            addApp(manage_py_path, "rest_framework")
            addApp(manage_py_path, "corsheaders")
            addMiddleware(manage_py_path, 'corsheaders.middleware.CorsMiddleware')
            addCode(manage_py_path, "cors")
        elif (status==1):
            os.chdir(project_check) 
            addApp(project_check, "rest_framework")
            addApp(project_check, "corsheaders")
            addMiddleware(project_check, 'corsheaders.middleware.CorsMiddleware')
            addCode(project_check, "cors")

    
    elif callName == "startapp":
        appName = sys.argv[2]
        if (status==0):
            subprocess.run(["django-admin", "startapp", appName], cwd=manage_py_path, check=True)
            addApp(manage_py_path, appName)
        
        elif (status==1):
            os.chdir(project_check) 
            subprocess.run(["django-admin", "startapp", appName], check=True)
            addApp(project_check, appName)

    
    elif callName == "addmultiuser":
        userList = sys.argv[2:]
        if (status==0):
            addCode(manage_py_path, "multiUser")
            multiUser(userList, manage_py_path)
        
        elif (status==1):
            os.chdir(project_check) 
            addCode(project_check, "multiUser")
            multiUser(userList, project_check)

    
    elif callName == "addscheduler":
        if (status==0):
            addCode(manage_py_path, "scheduler")
            scheduler(manage_py_path)
        elif (status==1):
            os.chdir(project_check) 
            addCode(project_check, "scheduler")
            scheduler(project_check)

    elif callName == "addmail":
        userList = sys.argv[2]
        if (status==0):
            addCode(manage_py_path, "mail")
            #addMail(manage_py_path)
        elif (status==1):
            os.chdir(project_check) 
            addCode(project_check, "mail")
           # addMail(project_check)

    elif callName == "addstatic":
        if (status==0):
            addCode(manage_py_path, "static")
            os.makedirs("media")
            os.makedirs("static")
            os.makedirs("templates")
            staticDirectories = ['img', 'js', 'css']
            for subdir in staticDirectories:
                subdirectory_path = os.path.join("static", subdir)
                os.makedirs(subdirectory_path)
            mediaDirectories = ['img', 'documents', 'audio','video']
            for subdir in mediaDirectories:
                subdirectory_path = os.path.join("static", subdir)
                os.makedirs(subdirectory_path)
        elif (status==1):
            os.chdir(project_check) 
            addCode(project_check, "static")
            os.makedirs("media")
            os.makedirs("static")
            os.makedirs("templates")
            staticDirectories = ['img', 'js', 'css']
            for subdir in staticDirectories:
                subdirectory_path = os.path.join("static", subdir)
                os.makedirs(subdirectory_path)
            mediaDirectories = ['img', 'documents', 'audio','video']
            for subdir in mediaDirectories:
                subdirectory_path = os.path.join("media", subdir)
                os.makedirs(subdirectory_path)

    