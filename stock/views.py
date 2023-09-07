from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser,DjangoModelPermissions
from .models import(
    Category,
    Brand,
    Product,
    Firm,
    Purchases,
    Sales,
    
)
from .serializers import(
    CategorySerializer,
    BrandSerializer,
    ProductSerializer,
    # Firm,
    # Purchases,
    # Sales,
    
)
# Create your views here.

class CategoryView(ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    permission_classes=[DjangoModelPermissions]
