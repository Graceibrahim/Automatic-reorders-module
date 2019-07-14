from django.contrib import admin

from .models import Product, Sales

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
	list_display = ("name", "units_of_measure", "price", "quantity", "default_quantity", "reorder_level")
	search_fields = ("name",)


admin.site.register(Product, ProductAdmin)