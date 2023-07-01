from django.db import models
from django.db.models import Sum

from project.models import BaseModel


class Department(BaseModel):
    title = models.CharField(verbose_name='Title', max_length=255)
    director = models.OneToOneField(
        'user.User',
        verbose_name='Director',
        on_delete=models.SET_NULL,
        null=True,
        related_name='+'
    )

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'

    def __str__(self):
        return self.title

    @property
    def total_salary(self) -> int:
        return int(self.employees.aggregate(total_salary=Sum('salary'))['total_salary'])

    @property
    def employees_count(self) -> int:
        return self.employees.count()
