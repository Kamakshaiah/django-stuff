from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Student, Course
from .forms import StudentForm, CourseForm

# Create your views here.
def home(request):
    return HttpResponse('this is home page')

def course_form(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
    else: 
        form = CourseForm()
    return render(request, 'students/course_form.html', {'form': form})

def student_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
    else: 
        form = StudentForm()
    return render(request, 'students/students_form.html', {'form': form})

def dashboard(request):
    studs = Student.objects.all()
    courses = Course.objects.all()
    context ={
        'students': studs,
        'courses': courses,
    }
    return render(request, 'students/dashboard.html', context)