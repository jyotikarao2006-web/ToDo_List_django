from django.db import models

# Create your models here.
class Task(models.Model):
    user1=models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    work=models.TextField()
    check1=[('Done', 'Done'), ('Not Done', 'Not Done'),('In Progress', 'In Progress')]
    status=models.CharField(max_length=20,choices=check1, default='Not Done')