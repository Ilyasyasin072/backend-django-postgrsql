from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import MovieSerializer, MovieMiniSerializer, CustomerSerializer, CustomerMiniSerializer, \
    SupplierSerialize, SupplierMiniSerializer, \
    InventorySerialize, InventoryMiniSerialize, \
    StockSerialize, StockMiniSerialize
from .models import Movie, Customer, Supplier, Inventory, Stock
from rest_framework.response import Response


class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def list(self, request, *args, **kwargs):
        movies = Movie.objects.all()
        serializer = MovieMiniSerializer(movies, many=True)
        return Response(serializer.data)


class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def list(self, request, *args, **kwargs):
        customers = Customer.objects.all()
        serializer = CustomerMiniSerializer(customers, many=True)
        return Response(serializer.data)


class SupplierViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerialize

    def list(self, request, *args, **kwargs):
        suppliers = Supplier.objects.all()
        serializer = SupplierMiniSerializer(suppliers, many=True)
        return Response(serializer.data)


class InventoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Inventory.objects.all()
    serializer_class = InventorySerialize

    def list(self, request, *args, **kwargs):
        inventories = Inventory.objects.all()
        serializer = InventoryMiniSerialize(inventories, many=True)
        return Response(serializer.data)


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerialize

    def list(self, request, *args, **kwargs):
        stocks = Stock.objects.all()
        serializer =  StockMiniSerialize(stocks, many=True)
        return Response(serializer.data)
