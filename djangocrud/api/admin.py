from django.contrib import admin
from .models import Movie, Customer, Supplier, Inventory, Stock
# Register your models here.
admin.site.register({Movie, Customer, Supplier, Inventory, Stock})
