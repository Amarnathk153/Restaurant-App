from .models import User, FoodItem, Order, ShippingAddress
from django import forms
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
    username = forms.CharField(label='', widget=forms.TextInput
                               (attrs={"placeholder": "UserName"}))
    first_name = forms.CharField(label='', widget=forms.TextInput
                                 (attrs={"placeholder": "First Name"}))
    last_name = forms.CharField(label='', widget=forms.TextInput
                                (attrs={"placeholder": "Last Name"}),
                                required=False)
    email = forms.EmailField(label='', widget=forms.EmailInput
                             (attrs={"placeholder": "Email"}))
    phone_number = forms.CharField(label='', widget=forms.TextInput
                                   (attrs={"placeholder": "Phone Number"}),
                                   required=False)
    password1 = forms.CharField(label='', widget=forms.TextInput
                                (attrs={"placeholder": "Set A Password"}))
    password2 = forms.CharField(label='', widget=forms.TextInput
                                (attrs={"placeholder": "Confirm Password"}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'last_name',
                  'phone_number', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already taken...")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already taken...")
        return email


class FoodItemForm(forms.ModelForm):
    name = forms.CharField(max_length=100, label='Name', widget=forms.TextInput
                           (attrs={"placeholder": "Name"}))
    price = forms.CharField(max_length=100, label='Price', widget=forms.
                            TextInput(attrs={"placeholder": "Price"}))
    image = forms.ImageField()

    class Meta:
        model = FoodItem
        fields = ("name", "price", "image")

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if FoodItem.objects.filter(name=name).exists():
            raise forms.ValidationError("Item already exist")
        return name


class OrderForm(forms.ModelForm):
    customer = forms.ModelChoiceField(queryset=User.objects.all(),
                                      widget=forms.HiddenInput())

    class Meta:
        model = Order
        fields = ("customer", "shipping_address", "food_item", "quantity",
                  "status")


class ShippingAddressForm(forms.ModelForm):
    customer = forms.ModelChoiceField(queryset=User.objects.all(),
                                      widget=forms.HiddenInput())

    class Meta:
        model = ShippingAddress
        fields = '__all__'
