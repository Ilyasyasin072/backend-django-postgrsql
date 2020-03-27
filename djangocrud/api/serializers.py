from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Movie, Customer, Supplier, Inventory, Stock


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'desc', 'year']


class MovieMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        # fields = ['id', 'title'] custome field views
        fields = ['id', 'title', 'desc', 'year']


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'address', 'tlp']


class CustomerMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        # fields = ['id', 'title'] custome field views
        fields = ['id', 'name', 'address', 'tlp']


class SupplierSerialize(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['id', 'name_supplier', 'company']


class SupplierMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        # fields = ['id', 'title'] custome field views
        fields = ['id', 'name_supplier', 'company']


class InventorySerialize(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['id', 'name', 'description', 'id_supplier']


class InventoryMiniSerialize(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['id', 'name', 'description', 'id_supplier']


class StockSerialize(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['id', 'stock', 'id_inventory']


class StockMiniSerialize(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['id', 'stock', 'id_inventory']
