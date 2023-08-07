from django.urls import include, path 
from . import views




#URLConf
urlpatterns = [
    path('get_course/matte1a',views.get_course, name='matte1a'),
    path('get_course/matte2a',views.get_course, name='matte2a'),
    path('get_course/matte3a',views.get_course, name='matte3a'),

    path('get_course/matte1b',views.get_course, name='matte1b'),
    path('get_course/matte2b',views.get_course, name='matte2b'),
    path('get_course/matte3b',views.get_course, name='matte3b'),
    
    path('get_course/matte1b',views.get_course, name='matte1c'),
    path('get_course/matte1b',views.get_course, name='matte2c'),
    path('get_course/matte1b',views.get_course, name='matte3c')
    ]