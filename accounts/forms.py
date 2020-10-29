from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from typing import Tuple, Dict
User = get_user_model()


class UserCreateForm(UserCreationForm):

    class Meta:
        model = User
        if User.USERNAME_FIELD == 'email':
            fields = ('email',)
        else:
            fields = ('username', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class UserSettingForm(forms.ModelForm):
    class Meta:
        model = User
        fields: Tuple[str, ...] = ('mycolor', 'accept_email', 'tz',)
        labels: Dict[str, str] = {
            'mycolor': 'カラー設定',
            'accept_email': 'メール通知の受取',
            'tz': 'タイムゾーン',
        }
        widgets = {
            'mycolor': forms.RadioSelect,
        }
