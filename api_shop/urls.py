from rest_framework import routers
from django.urls import path, include
from .views import *

router = routers.SimpleRouter()
router.register('cars', CarViewSet, basename='cars')
router.register('brands', BrandViewSet, basename='brands')
router.register('customers', CustomerViewSet, basename='customers')
router.register('employees', EmployeeViewSet, basename='employees')
router.register('sales', SaleViewSet, basename='sales')
router.register('testdrives', TestDriveViewSet, basename='testdrives')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
] 

