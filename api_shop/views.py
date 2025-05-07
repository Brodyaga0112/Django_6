from rest_framework import viewsets
from .serializers import *
from .permissions import CustomPermissions, PaginationPage
from shop.models import Car, Brand, Customer, Employee, Sale, TestDrive

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

    def get_queryset(self):
        queryset = Car.objects.all()
        model = self.request.query_params.get('model', None)
        brand = self.request.query_params.get('brand', None)
        
        if model:
            queryset = queryset.filter(model__icontains=model)
        if brand:
            queryset = queryset.filter(brand__name__icontains=brand)
        
        return queryset

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class TestDriveViewSet(viewsets.ModelViewSet):
    queryset = TestDrive.objects.all()
    serializer_class = TestDriveSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage 