import os
import sys
import subprocess
from .addInstallApp import addApp
def multiUser(userList,projectName):
    subprocess.call(["django-admin", "startapp", "accounts"])
    addApp(projectName,"accounts")
    os.chdir("accounts") 
    addModels(userList)
    addAdmin(userList)
    os.chdir(os.path.dirname(os.getcwd()))
    subprocess.call(["python", "manage.py", "makemigrations", "accounts"])
    subprocess.call(["python", "manage.py", "migrate", "accounts"])

def addModels(userList):
    path = "models.py"
    code1 = f'''\
\n
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
'''    
    with open(path, "a") as file:
        file.write(code1)


    for i in userList:
        code2 = f'''\
    is_{i} = models.BooleanField(default=False)
''' 
        with open(path, "a") as file:
            file.write(code2)


def addAdmin(userList):
    path = "admin.py"
    code1 = '''\
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        ('ACCOUNT', {'fields': ('username', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('ACCOUNT STATUS', {'fields': ('last_login', 'date_joined', 'is_active')}),
        ('USER TYPE', {'fields': (
'''
    with open(path, "a") as file:
        file.write(code1)

    with open(path, "a") as file:
        for userType in userList:
            code2 = f"'is_{userType}',"
            file.write(code2)

        code3 = '''\
        )}),
    )
'''
        file.write(code3)



