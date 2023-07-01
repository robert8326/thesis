from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.department.models import Department


class User(AbstractUser):
    first_name = models.CharField(verbose_name="First name", max_length=150)
    last_name = models.CharField(verbose_name="Last name", max_length=150)
    patronymic = models.CharField(verbose_name="Patronymic", max_length=150)
    avatar = models.ImageField(verbose_name='Avatar', upload_to='avatars/', blank=True, null=True)
    position = models.CharField(verbose_name='Position', max_length=100)
    salary = models.DecimalField(verbose_name='Salary', decimal_places=3, max_digits=15, blank=True, null=True)
    age = models.PositiveIntegerField(verbose_name='Age', blank=True, null=True)
    department = models.ForeignKey(
        Department,
        verbose_name='Department',
        related_name='employees',
        on_delete=models.CASCADE,
        blank=True, null=True
    )

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self) -> str:
        if self.patronymic and self.last_name and self.first_name:
            return f'{self.first_name} {self.last_name} {self.patronymic}'
        return self.username

    def get_full_name(self) -> str:
        return f'{self.first_name} {self.last_name} {self.patronymic}'
