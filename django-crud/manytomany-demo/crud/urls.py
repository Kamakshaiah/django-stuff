
from django.contrib import admin
from django.urls import path, include
from students import urls as student_urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(student_urls)),
]
