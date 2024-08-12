from django import forms
from django.contrib.auth.models import User
from .models import Contact


class AddcontactForm(forms.ModelForm):
 class Meta:
    model=Contact
    fields=["name","email","phone"]
    widgets={
            "name":forms.TextInput(attrs={"class":"form-control","placeholder":"name"}),
            "email":forms.TextInput(attrs={"class":"form-control","placeholder":"email"}),
            "phone":forms.TextInput(attrs={"class":"form-control","placeholder":"phone"}),
    }

       

           
class ContactUpdateForm(forms.ModelForm):
     class Meta:
          model=Contact
          fields=["name","email","phone"]
          widgets={
                "name":forms.TextInput(attrs={"class":"form-control","placeholder":"name"}),
                "phone":forms.TextInput(attrs={"class":"form-control","placeholder":"email"}),
                "email":forms.TextInput(attrs={"class":"form-control","placeholder":"phone"}),
                 



            }
        