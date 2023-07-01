from django.urls import path

from apps.department.views import DepartmentAPIView

urlpatterns = [
    path('departments/', DepartmentAPIView.as_view(), name='department'),
]
