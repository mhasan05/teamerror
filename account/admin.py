from django.contrib import admin
from account.models import UserAccount
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group


class UserAccountAdmin(UserAdmin):
    search_fields = ('username','phone')

    list_display = ['username','first_name','last_name','designation','is_active']
    fieldsets = UserAdmin.fieldsets + (
            ('Account Summary', {'fields': ('profile_pic','designation','phone_home','phone_office',)}),
    )

    add_fieldsets = (
            (
                None,
                {
                    'classes': ('wide',),
                    'fields': ('profile_pic','username', 'first_name', 'last_name','designation','email','phone_home','phone_office', 'password1', 'password2'),
                },
            ),
        )
    ordering = ('-date_joined',)
    
admin.site.register(UserAccount,UserAccountAdmin)
admin.site.unregister(Group)