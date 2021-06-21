from django import forms
from .models import CustomUser


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():  # bootstrapで使用するform-controlクラス
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = CustomUser
        fields = ('nickname', 'email', 'avatar')
        help_texts = {
            'nickname': "ユーザーネーム",
            'email': None,
        }
