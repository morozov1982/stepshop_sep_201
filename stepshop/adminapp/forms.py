from django import forms
from authapp.models import ShopUser
from django.contrib.auth.forms import UserChangeForm


class ShopUserAdminEditForm(UserChangeForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'is_superuser', 'is_staff', 'is_active', 'is_deleted',
                  'first_name', 'last_name', 'email', 'age', 'avatar')
        # fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.help_text = ''
