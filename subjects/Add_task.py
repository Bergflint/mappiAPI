import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mappiAPI.settings')
django.setup()

from subjects.models import Task

def add_task():
    task_id = input('task_id')
    date = input('date')
    image_id = input('image_id')
    your_solution_id = input('your_solution_id')


    course_data = {
        'task_id': str(task_id),
        'date': str(date),  # Replace with the desired date format
        'image_id': str(image_id),
        'solution_id': str(your_solution_id),
        #'theoryimage_id': str(theoryimage_id),
        #'difficulty': str(difficulty),  # Replace with the desired difficulty level
        'description': 'Your course description goes here.',
    }

    Task.objects.create(
        task_id=course_data['task_id'],
        date=course_data['date'],
        image_id=course_data['image_id'],
        solution_id=course_data['solution_id'],
        theoryimage_id=course_data['theoryimage_id'],
        difficulty=course_data['difficulty'],
        description=course_data['description'],
    )

if __name__ == '__main__':
    add_task()
