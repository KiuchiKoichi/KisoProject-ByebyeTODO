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
            'mycolor': 'テーマカラー選択',
            'accept_email': 'メール通知の受け取り',
            'tz': 'タイムゾーン設定',
        }
        widgets = {
            'mycolor': forms.RadioSelect,
        }
        #choice = forms.ChoiceField(label='radio', \choices=COLOR_CHOICES, widget=forms.RadioSelect())
    '''class ColorForm(forms.Form):
        color = forms.ModelChoiceField(queryset=Color.objects.all(),
        empty_label=None,
        required=False, 
        )'''
