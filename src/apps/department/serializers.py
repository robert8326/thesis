from rest_framework import serializers

from apps.department.models import Department
from apps.user.serializers import UserSerializer


class DepartmentSerializer(serializers.ModelSerializer):
    director = UserSerializer()

    class Meta:
        model = Department
        fields = ('id', 'title', 'director', 'employees', 'employees_total_salary', 'employees_count')
