from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import CourseForm
from .models import course
# Create your views here.

def course_view(request):
    
    if request.method == 'POST':
        form = CourseForm(request.POST)
       
        if form.is_valid():
            form.save()
        return redirect('course_description')

    else: 
        form = CourseForm()
    
    context = {
        'form': form
    }
    
    return render(request, 'courses/course.html', context)

def course_description(request):
    courses = course.objects.all()
    # for c in courses:
    #     print(c.name)
    context = {
        'courses': courses
    }
    return render(request, 'courses/course_description.html', context) 

def course_name_list(request):
    names = []
    courses = course.objects.all()
    # for c in courses:
    #     names.append(c.name)
    return render(request, 'courses/course_names.html', {'names': courses})

def single_course_description(request, course_name):
    single_course = course.objects.get(name=course_name)
    return render(request, 'courses/course_names.html', {'scn': single_course})