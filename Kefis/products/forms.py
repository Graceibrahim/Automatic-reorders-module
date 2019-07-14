from django import forms
from .models import Product, Sales

class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = "__all__"


class SalesForm(forms.ModelForm):
	class Meta:
		model = Sales
		fields = "__all__"		