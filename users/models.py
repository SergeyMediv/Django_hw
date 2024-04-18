from django.contrib.auth.models import AbstractUser
from django.db import models

from catalog.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=35, verbose_name='Email', unique=True)
    phone = models.CharField(max_length=35, verbose_name='Телефон', **NULLABLE, help_text='Номер телефона')
    country = models.CharField(max_length=35, verbose_name='Страна', **NULLABLE, help_text='Страна')
    avatar = models.ImageField(upload_to='users/', verbose_name='Автатар', **NULLABLE, help_text='Ваш аватар')

    token = models.CharField(max_length=35, verbose_name='token', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
