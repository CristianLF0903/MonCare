from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from login.models import Usuario

# Register your models here.


class AccountInLine(admin.StackedInline):
    model = Usuario
    can_delete = False
    verbose_name_plural = 'Usuarios'


class CustomizedUserAdmin(UserAdmin):
    inlines = (AccountInLine, )


admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)
