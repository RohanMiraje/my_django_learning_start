from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    # image = models.FilePathField(path='/projects/img')
    image = models.CharField(max_length=100)
# Project(title='Test project',description='This is I am learning Django', technology='Django', image='test1.png')