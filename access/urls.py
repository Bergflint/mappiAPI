from django.urls import include, path #
from . import views #Hämtar wiev-modulen så att vi kan använda view-funktioner


#URLConf
urlpatterns = [
    #path: först skrivs routen; url-idn, sen skrivs funktionen från views
    #View-funktion behövs inte kallas på med ()
    #Varje url måste avslutas med en backslash
    path('register/',views.sign_up,name='register'),
    path('login/',views.log_in,name='login'),
    ]


