from django import forms

from .models import Vehicle, Category


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = [
            'name',
            'year',
            'selling_price',
            'km_driven',
            'transmission',
            'category'
        ]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'name'
        ]
