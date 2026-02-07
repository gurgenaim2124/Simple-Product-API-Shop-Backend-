from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticated

class ProductList(generics.ListAPIView):
    # queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        category = self.request.query_params.get('category', None)
        if category:
            return Product.objects.filter(category__name=category)
        return Product.objects.all()

class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


    # class ProductList(generics.ListAPIView):
    #     serializer_class = ProductSerializer

    # def get_queryset(self):
    #     category = self.request.query_params.get('category', None)
    #     if category:
    #         return Product.objects.filter(category__name=category)
    #     return Product.objects.all()