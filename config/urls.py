from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('mailling/', include('mailling.urls'), name='mailling'),
    path('users/', include('users.urls'), name='users'),
]

