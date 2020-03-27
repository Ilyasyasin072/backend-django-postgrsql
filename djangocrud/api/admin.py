from django.contrib import admin
from .models import Movie, Customer, Supplier, Inventory
# Register your models here.
admin.site.register({Movie, Customer, Supplier, Inventory})
