# Owned by Yash Jangid 
# github_id = yash-jangid-21
# linkeldn_id = yash-21-yash
from django.db import models

class Task(models.Model):
    task_name = models.CharField(max_length=30)
    task_priority = models.CharField(max_length=10)
    task_duedate = models.CharField(max_length=10)