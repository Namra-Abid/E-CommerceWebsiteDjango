from django import forms
from django.forms import ValidationError
from .models import Customer

class CustomerForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email','phone','password']
    # this function will be used for the validation
    def clean(self):
        
        form_data = self.cleaned_data
        if len(form_data['first_name']) < 4:
            self._errors["first_name"] = ["First Name Should be atleast 4 characters"] # Will raise a error message
            del form_data['first_name']
        if len(form_data['last_name']) < 4:
            self._errors["last_name"] = ["Last Name Should be atleast 4 characters"] # Will raise a error message
            del form_data['last_name']
        if len(form_data['phone']) < 11:
            self._errors["phone"] = [" Should be atleast 10 characters"] # Will raise a error message
            del form_data['phone']
        if Customer.objects.filter(email=form_data['email']).exists():
            self._errors["email"] = [" Email should be unique"] # Will raise a error message
            del form_data['email']

        
        # if form_data['first_name'] != form_data['last_name']:
        #     self._errors["first_name"] = ["Password do not match"] # Will raise a error message
        #     del form_data['first_name']
        return form_data

    

