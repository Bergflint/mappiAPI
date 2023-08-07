from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.



def get_course(request, course):
    if request.method == "GET":
        print(course)
    return JsonResponse({'superuser_name': 'superusers_name'})