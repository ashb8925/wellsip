from django import forms
from . import models

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())


class RegisterForm(forms.Form):
    full_name = forms.CharField(max_length=100, required=True, label="Full Name")
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)

    class Meta:
        model = models.UsersModel
        fields = ['email', 'password']

    def clean_full_name(self):
        full_name = self.cleaned_data.get("full_name").strip()
        name_parts = full_name.split()
        first_name = name_parts[0]
        last_name = " ".join(name_parts[1:]) if len(name_parts) > 1 else ""
        return {"first_name": first_name, "last_name": last_name}

    def save(self):
        cleaned_data = self.cleaned_data
        name_data = cleaned_data.get("full_name")

        user = models.UsersModel(
            first_name=name_data["first_name"],
            last_name=name_data["last_name"],
            email=cleaned_data["email"],
            password=cleaned_data["password"],  # Consider hashing this before saving
        )
        user.save()
        return user