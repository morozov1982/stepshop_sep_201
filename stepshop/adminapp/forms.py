from django import forms
from authapp.models import ShopUser
from django.contrib.auth.forms import UserChangeForm


class ShopUserAdminEditForm(UserChangeForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'is_superuser', 'is_staff', 'is_active', 'is_deleted',
                  'first_name', 'last_name', 'email', 'age', 'avatar')
        # fields = '__all__'
