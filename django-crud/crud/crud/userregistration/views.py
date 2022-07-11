from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import User
from .forms import UserRegistrationForm

# Create your views here.
def home(request):
    return render(request, 'userregistration/home.html')

def add(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        form = UserRegistrationForm()
    else:
        form = UserRegistrationForm()
    return render(request, 'userregistration/add.html', {'form': form})

def show(request):
    users = User.objects.all()
    context = {
        'users': users,
    } 
        
    return render(request, 'userregistration/show.html', context)

def update(request, id):
    if request.method == 'POST':
        user = User.objects.get(pk=id)
        form = UserRegistrationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('show')
    else:
        user = User.objects.get(pk=id)
        form = UserRegistrationForm(instance=user)
    return render(request, 'userregistration/updateform.html', {'form': form})

def delete(request, id):
    user = User.objects.get(pk=id)
    user.delete()
    return redirect('show')

def authenticate(request, id):
    user = User.objects.get(pk=id)
    user.is_authenticated = True
    user.save()
    return redirect('show')