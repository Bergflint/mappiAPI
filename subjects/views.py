from django.shortcuts import render
from django.http import JsonResponse
from .models import Course,Field,Task

# Create your views here.



def get_course(request, course):
    if request.method == "GET":
        print(course)
        name = Field.objects.filter(course_id=course).first().name
        id = Field.objects.filter(course_id=course).first().id
        
    return JsonResponse({'id': id,'name':name})