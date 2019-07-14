from django.urls import path
from .views import add_product, list_products, sell_product, unprocessed_reorders, dispatch_reorder



urlpatterns = [
	path('add/', add_product, name="add_product"),
	path('list/', list_products, name="list_products"),
	path('sell/<int:pk>/', sell_product, name="sell_product"),
	path('reorders/', unprocessed_reorders, name="unprocessed_reorders"),
	path('dispatch/', dispatch_reorder, name="dispatch_reorder"),
]