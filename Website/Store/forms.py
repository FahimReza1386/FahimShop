from django.contrib.auth.models import User
from django.contrib.auth.forms import  UserCreationForm , UserChangeForm , SetPasswordForm
from django import forms

class RegisterForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(RegisterForm , self).__init__(*args , **kwargs)
        for item in self.visible_fields():
            item.field.widget.attrs['class'] = 'form-control'
            item.field.widget.attrs['style'] = 'text-align: center;'

    first_name = forms.CharField(required=True , label='First_Name')
    last_name = forms.CharField(required=False , label='Last_Name')
    email = forms.EmailField(required=True , widget=forms.TextInput() , label='Email')
    username = forms.CharField(required=True , label='Username' , max_length=50 , min_length=5)
    password1 = forms.CharField(required=True , label='Password' , widget=forms.PasswordInput() , max_length=50)
    password2 = forms.CharField(required=True , label='Confirm Password' , widget=forms.PasswordInput() , max_length=50)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1')



class UpdateUserForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)
        for item in self.visible_fields():
            item.field.widget.attrs['class'] = 'form-control'
            item.field.widget.attrs['style'] = 'text-align: center;'

    # Hide Password Stuff
    password = None
    # Get Other Fields

    first_name = forms.CharField(required=True, label='First_Name')
    last_name = forms.CharField(required=False, label='Last_Name')
    email = forms.EmailField(required=True, widget=forms.TextInput(), label='Email')
    username = forms.CharField(required=True, label='Username', max_length=50, min_length=5)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')



class UpdatePassword(SetPasswordForm):

    def __init__(self, *args, **kwargs):
        super(UpdatePassword , self).__init__(*args , **kwargs)
        for item in self.visible_fields():
            item.field.widget.attrs['class'] = 'form-control'
            item.field.widget.attrs['style'] = 'text-align: center;'

    class Meta:
        model = User
        fields = ('new_password1', 'new_password2')