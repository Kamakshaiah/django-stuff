from django.contrib import admin
from django.urls import path, include
from home import urls as home_urls
from accounts import urls as account_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(home_urls)),
    path('accounts/', include(account_urls)),
]
