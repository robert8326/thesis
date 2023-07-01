from django.urls import path

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from apps.user.views import (
    RegisterUserAPIView,
    UserViewSet, DepartmentEmployeesAPIView
)

router = DefaultRouter()
router.register('employee', UserViewSet)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('employee/register/', RegisterUserAPIView.as_view(), name='register'),
    path('employees/<int:department_id>/', DepartmentEmployeesAPIView.as_view(), name='department employees')
]

urlpatterns += router.urls
