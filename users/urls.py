from django.contrib import admin
from django.urls import path, include

from mailling.views import HomeListView
from users.views import UserCreateView, CustomLoginView

app_name = 'users'

urlpatterns = [
    path('register/', UserCreateView.as_view(template_name='register.html'), name='register'),
    path('login/', CustomLoginView.as_view(template_name='login.html'), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    ]
