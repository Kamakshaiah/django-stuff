from django.urls import reverse_lazy
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), name='password_change'),
    path('password_change_done', auth_views.PasswordChangeView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),
    path('password_reset', auth_views.PasswordResetView.as_view(template_name="registration/password_reset_form.html"), name="password_reset"),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"), name="password_reset_confirm"), 
    path('password_reset_done', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html"), name="password_reset_complete"),
]
