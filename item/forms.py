from django import forms
from .models import Item
from item.models import Category

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image')

    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Name',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))
    description = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Description',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))
    price = forms.DecimalField(widget=forms.TextInput(attrs={
        'placeholder': 'Price',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'w-full py-4 px-6 rounded-xl',
    }))
    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={
        'class': 'w-full py-4 px-6 rounded-xl',
    }))