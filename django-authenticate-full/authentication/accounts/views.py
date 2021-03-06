from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)   
        # username = request.POST['username']
        # password = request.POST['password1']
        # print(username, password)
        if form.is_valid():
            form.save()
    else: 
        form = UserCreationForm()

    context = {
        'form':form
    }
    return render(request, 'registration/register.html', context)