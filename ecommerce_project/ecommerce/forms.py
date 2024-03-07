from django import forms
from .models import Product, Customer, Order
from django.core.validators import EmailValidator, RegexValidator

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

# class CustomerForm(forms.ModelForm):
#     class Meta:
#         model = Customer
#         fields = '__all__'


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = '__all__'
        
        widgets = {
            'phone_number': forms.TextInput(attrs={'pattern': '^(\+?\d{1,3}\-)?\d{9,15}$'})
        }
        labels = {
            'phone_number': 'Phone Number',
        }
        validators = {
            'email': EmailValidator(message="Please enter a valid email address."),
            'phone_number': RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
        }

    def clean(self):
        cleaned_data = super().clean()
        for field_name, field_value in cleaned_data.items():
            if not field_value:
                raise forms.ValidationError(f"{field_name.capitalize()} is required.")
        return cleaned_data
    

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
