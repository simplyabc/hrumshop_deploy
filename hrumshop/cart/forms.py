from django import forms
from .models import Order


class OrderAddForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['id', 'name', 'phone', 'address', 'comments']