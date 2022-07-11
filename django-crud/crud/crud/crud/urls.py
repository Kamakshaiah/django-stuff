
from django.contrib import admin
from django.urls import path, include
from userregistration import urls as userregurls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(userregurls)),

]
