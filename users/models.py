from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(unique=True, blank=True, null=True)
    email = models.EmailField(unique=True, verbose_name='Email',)
    avatar = models.ImageField(upload_to='../media/users/', blank=True, null=True, verbose_name='Аватар',)
    phone = models.CharField(max_length=11, blank=True, null=True, verbose_name='Номер телефона',)
    country = models.CharField(max_length=50, blank=True, null=True, verbose_name='Страна')
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'