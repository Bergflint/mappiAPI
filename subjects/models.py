from django.db import models

# Create your models here.

class Course(models.Model):
    course_id = models.CharField(max_length=100)
    description = models.TextField()
    image_id = models.CharField(max_length=100)

    def __str__(self):
        return self.course_id
    
class Field(models.Model):
    id = models.CharField(max_length=100)
    name = models.TextField()
    course_id = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Task(models.Model):
    task_id = models.CharField(max_length=100)
    date =  models.CharField(max_length=100)
    image_id = models.CharField(max_length=100)
    solution_id =  models.CharField(max_length=100)
    theoryimage_id =  models.CharField(max_length=100)
    difficulty =  models.CharField(max_length=100)
    discription =  models.CharField(max_length=100)

    def __str__(self):
        return self.task_id

