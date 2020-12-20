from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

lst_user =[("Admin","Admin"),("Mitra","Mitra"),("Lembaga Sosial","Lembaga Sosial"),("Kontributor/Pembeli","Kontributor/Pembeli")]

class SignUpForm(UserCreationForm):
    role = forms.ChoiceField(label='Role', choices=lst_user)

    class Meta:
        model = User
        fields = ("username", "role", "password1", "password2")