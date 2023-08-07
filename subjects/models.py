from django.db import models

# Create your models here.

class Course(models.Model):
    course_id = models.CharField(max_length=100)
    description = models.TextField()
    image_id = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class Field(models.Model):
    field_id = models.CharField(max_length=100)
    description = models.TextField()
    image_id = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class Task(models.Model):
    task_id = models.CharField(max_length=100)
    date =  models.CharField(max_length=100)
    image_id = models.CharField(max_length=100)
    solution_id =  models.CharField(max_length=100)
    theoryimage_id =  models.CharField(max_length=100)
    difficulty =  models.CharField(max_length=100)
    discription =  models.CharField(max_length=100)

    def __str__(self):
        return self.title

