from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.validators import ValidationError

from apps.department.models import Department
from apps.user.models import User
from apps.user.serializers import (
    RegisterUserSerializer,
    UserSerializer
)


class RegisterUserAPIView(generics.CreateAPIView):
    """ User registration """
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterUserSerializer


class UserViewSet(ModelViewSet):
    """ User get, update, delete """
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = LimitOffsetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['department_id', 'first_name']
    serializer_class = UserSerializer
    http_method_names = ('get', 'patch', 'delete')


class DepartmentEmployeesAPIView(generics.GenericAPIView):
    """ Return of deportation employees """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, *args, **kwargs):
        department_id = kwargs.get('department_id')
        if not department_id:
            raise ValidationError({'detail': 'Parameter department_id required'})
        department = get_object_or_404(Department, id=department_id)
        users = self.queryset.filter(department=department)
        serializer = self.serializer_class(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
