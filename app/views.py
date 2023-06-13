from django.shortcuts import render

# Create your views here.
from app.models import *
from rest_framework import viewsets
from app.serializers import *

class ProductCrudMVS(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer