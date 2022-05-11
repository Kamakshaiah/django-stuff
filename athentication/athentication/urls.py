
from django.contrib import admin
from django.urls import path, include
from accounts import urls as accounts_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(accounts_urls)),
]
