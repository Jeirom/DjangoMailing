from django.urls import path
from users.apps import UsersConfig
from users.views import UserCreateView, CustomLogoutView, CustomLoginView

app_name = UsersConfig.name

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', UserCreateView.as_view(), name='register'),
]