from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
	email=forms.EmailField()
	class Meta:
		model=User
		fields=["first_name","last_name","username", "email", "password1","password2"]
		#fields = "__all__"

class RegisterForm2(UserCreationForm):
    username = forms.CharField(max_length = 100)
    email  = forms.EmailField(max_length = 100)
    password1 = forms.CharField(widget = forms.PasswordInput() , max_length = 100)
    password2 = forms.CharField(widget = forms.PasswordInput(),  max_length = 100)
    first = forms.CharField(max_length = 100 )
    last = forms.CharField(max_length = 100)

    class Meta  : 
        fields = "__all__"
        
    def clean_username(self):
        username = self.cleaned_data.get("username")
        if not username : 
            raise forms.ValidationError("UserName cannot be empty !")

        try : 
            user = User.objects.get(username = username)
        except :
            user = None

        if user : 
            raise forms.ValidationError("User with the username -: {} already exits ".format(username))

        return username    

    def clean_first(self) :
        first = self.cleaned_data.get("first")
        if not first: 
            raise forms.ValidationError("Kindly enter your first name !")
            
    def clean_last(self) :
        last = self.cleaned_data.get("last")
        if not last: 
            raise forms.ValidationError("Kindly enter your last name !")

    # in what ever field you want to apply validations and authentications create a function named "clean_{field_name}" and get the data from the cleaned_data attribute 