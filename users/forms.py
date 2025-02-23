from django.contrib.auth.forms import UserCreationForm
from users.models import Users
from mailling.forms import StyleFormMixin


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = Users
        fields = ("email", "password1", "password2","country")
