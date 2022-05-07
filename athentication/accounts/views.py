from curses.ascii import US
from email import contentmanager
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request, 'accounts/home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        uname = form.data['username']
        pword = form.data['password1']
        print(uname, pword)
        if form.is_valid():
            form.save()
        return HttpResponse(f'{uname}! You have been registered successfully.')
    else: 
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'register/register.html', context)

def login_user(request):
    if request.method == 'POST':
        uname = request.POST['username']
        user = User.objects.get(username=uname)
        # user = authenticate(username = user.username, password=user.password)
        login(request, user)
        return redirect('home')
    
    return render(request, 'register/login.html')

def logout_user(request):
    user = request.user
    logout(request)
    return HttpResponse(f'{user} has been logout!')