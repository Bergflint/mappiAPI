from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.shortcuts import redirect
from django.contrib.auth.models import User



# Create your views here.
#view function tar en request och skapar en respons (händelse)

#Views är det som faktsikt gör att saker händer - URLS kallar på views
#En request-hanterare (Action)


def sign_up(request):
    print("hej")
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            render(request, 'access/index.html', {'form':form}) #här skickas informationen i formuläret tillbaka genom en dictionary
        else:
            print(form.errors)
            form = SignUpForm()
            return render(request, 'access/signup.html', {'form':form})
        
        
        return redirect('loginpage')
    else:
        return render(request, 'access/signup.html', {'form':form})
        


def log_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username,password=password)
        if user is not None:
            print(user)
            login(request,user)
            return redirect('homepage')
        else:
            print('inget konto')
            return redirect('loginpage')
    else:
        return render(request, 'access/index.html') 
    
           

    




def test(request): #Tar in en request, skickar ut en response
    #En function som till exemepel kan hämta data från databad, ändra data, skicka email
    superusers = User.objects.filter(is_superuser=True)
    print(superusers)
    return str(superusers) #Denna function med specifik respons måste kopplas till en url så att när en användare går in på den url:en så startar funktionen och rätt respons ges 
