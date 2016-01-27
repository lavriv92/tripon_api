from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import PaymentPlan, User
from .forms import UserCreationForm, UserChangeForm

class UserAdmin(BaseUserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm


    last_display = ('email', 'username', 'first_name', 'last_name', 'created',)
    list_filter = ('is_admin', 'is_active',)

    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal Info', {
            'fields': ('first_name', 'last_name', 'payment_plan', )
        }),
        ('Permissions', {'fields': ('is_active', 'is_admin', )}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', )}
        ),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.unregister(Group)

admin.site.register(PaymentPlan)
admin.site.register(User, UserAdmin)
