    
import os
import fileinput

def addCode(FileName,type):
    if(type=="cors"):
        addCors(FileName)
    elif(type=="multiUser"):
         addMultiUser(FileName)
    elif(type=="scheduler"):
         addScheduler(FileName)
    elif(type=="mail"):
         addMail(FileName)
    elif(type=="static"):
         addStatic(FileName)
   
def addCors(FileName):
    path = os.path.join(FileName, "settings.py")
    CORS_ORIGIN_WHITELIST = f'''\
\n
CORS_ORIGIN_WHITELIST = [
'http://localhost:3000',
]
    '''
    with open(path, "a") as file:
        file.write(CORS_ORIGIN_WHITELIST)


def addMultiUser(FileName):
    path = os.path.join(FileName, "settings.py")
    AUTH_USER_MODEL = f'''\
\n
AUTH_USER_MODEL = 'accounts.User'
    '''
    with open(path, "a") as file:
        file.write(AUTH_USER_MODEL)

def addScheduler(FileName):
    path = os.path.join(FileName, "settings.py")
    SCHEDULER_DEFAULT = f'''\
\n
SCHEDULER_DEFAULT = True
    '''
    with open(path, "a") as file:
        file.write(SCHEDULER_DEFAULT)

def addMail(FileName):
    path = os.path.join(FileName, "settings.py")
    EMAIL = f'''\
\n
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_HOST = 'smtp.example.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
#EMAIL_HOST_USER = 'sample@example.com'
#EMAIL_HOST_PASSWORD = 'abcdefg'
\n
    '''
    with open(path, "a") as file:
        file.write(EMAIL)


def addStatic(FileName):
    path = os.path.join(FileName, "settings.py")
    with open(path, 'r') as file:
        lines = file.readlines()
    for i, line in enumerate(lines):
        if line.strip() == "from pathlib import Path":
            lines.insert(i + 1, '\nimport os')
            break
    with open(path, "w") as file:
        file.writelines(lines)

  
    find_string = "        'DIRS': [],"
    replace_string = "        'DIRS': [os.path.join(BASE_DIR, 'templates')],"
    replaces(path,find_string,replace_string)

    find_string = "STATIC_URL = 'static/'"
    replace_string = " "
    replaces(path,find_string,replace_string)

    static = f'''\
\n

# Specify the URL prefix for static files (CSS, JavaScript, images)
STATIC_URL = '/static/'

# Specify the directory where your static files will be collected
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Specify the directory where your static files are located
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Specify the URL prefix for media files (user-uploaded files)
MEDIA_URL = '/media/'

# Specify the directory where media files will be uploaded
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

\n
    '''
    with open(path, "a") as file:
        file.write(static)





def replaces(path,find_string,replace_string):
    for line in fileinput.input(path, inplace=True):
        line = line.replace(find_string, replace_string)
        print(line, end='')


        