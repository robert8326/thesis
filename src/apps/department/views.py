from rest_framework.permissions import AllowAny
from rest_framework.generics import ListAPIView

from apps.department.models import Department
from apps.department.serializers import DepartmentSerializer


class DepartmentAPIView(ListAPIView):
    """ Departments list """
    queryset = Department.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = DepartmentSerializer
    pagination_class = None
