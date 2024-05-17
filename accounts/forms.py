from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreation(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ["username", "email", "name"] #type: ignore