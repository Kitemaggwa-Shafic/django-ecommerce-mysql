from django import forms
from .models import Product

# Creating a productForm inheritating from (forms.modelForms)
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['image', 'name', 'price', 'description', 'is_published']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'formcontrol'}),
            'name': forms.TextInput(attrs={'class': 'formcontrol'}),
            'price': forms.TextInput(attrs={'class': 'formcontrol'}),
            'description': forms.TextInput(attrs={'class': 'formcontrol'}), 
        }
