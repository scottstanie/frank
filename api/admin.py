from django.contrib import admin
from django import forms

# Admin workaround for AbstractUser
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from api.models import User, Question, Showdown, Friend

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User

@admin.register(User)
class MyUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('custom_data',)}), # input custom fields here
    )


admin.site.register(Question)
admin.site.register(Showdown)
admin.site.register(Friend)
