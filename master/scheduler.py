import os
import sys
import subprocess
from .addInstallApp import addApp
def scheduler(projectName):
    subprocess.call(["django-admin", "startapp", "scheduler"])
    addApp(projectName,"scheduler")
    os.chdir("scheduler") 
    addModels()
    addAdmin()
    os.chdir(os.path.dirname(os.getcwd()))
    subprocess.call(["python", "manage.py", "makemigrations", "scheduler"])
    subprocess.call(["python", "manage.py", "migrate", "scheduler"])
    os.chdir("scheduler") 
    addJobs()
    addScheduler()
    addEntry()
    os.chdir(os.path.dirname(os.getcwd()))

def addModels():
    path = "models.py"
    code = f'''\
\n
class Job(models.Model):
    job_name = models.CharField(max_length=100)
    def __str__(self):
        return self.job_name
\n
class JobExecution(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    runtime = models.DateTimeField(auto_now_add=True)
    error = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=100)
    def __str__(self):
        return f"{{self.job}} - {{self.runtime}}"
'''    
    with open(path, "a") as file:
        file.write(code)



def addAdmin():
    path = "admin.py"
    code = '''\
from .models import Job,JobExecution
\n
admin.site.register(Job)
admin.site.register(JobExecution)
'''    

    with open(path, "a") as file:
        file.write(code)




def addJobs():
    path = "jobs.py"
    code = '''\
def printHi():
    print("Hi i am Django")
'''    

    with open(path, "w") as file:
        file.write(code)


def addScheduler():
    path = "scheduler.py"
    code = '''\
from apscheduler.schedulers.background import BackgroundScheduler
from .models import Job, JobExecution
from django.utils import timezone
from .jobs import *

scheduler = BackgroundScheduler(timezone=timezone.get_current_timezone())

def schedule_job(job_name, function, schedule_type, **kwargs):
    job, created = Job.objects.get_or_create(job_name=job_name)
    if created or Job.objects.filter(job_name=job).exists():
        scheduler.add_job(run_job, schedule_type, args=[job, function], **kwargs)

def run_job(job, function):
    job_execution = JobExecution.objects.create(job=job, status='running')
    try:
        function()
        job_execution.status = 'success'
    except Exception as e:
        job_execution.error = str(e)
        job_execution.status = 'failed'
    finally:
        job_execution.save()

# Schedule the cron job
schedule_job('printHi_cron', printHi, 'cron', year='*', day=1, month=1, hour=7, minute=0, second=0)

# Schedule the interval job
schedule_job('printHi_interval', printHi, 'interval', minutes=1, seconds=30)

# Start the scheduler
scheduler.start()
'''    

    with open(path, "w") as file:
        file.write(code)

def addEntry():
    path = "apps.py"
    code = '''\
from django.apps import AppConfig
from django.conf import settings

class SchedulerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'scheduler'
    def ready(self):    
        if settings.SCHEDULER_DEFAULT:
            from . import scheduler
'''    

    with open(path, "w") as file:
        file.write(code)