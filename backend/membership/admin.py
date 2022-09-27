from django.contrib import admin
from . models import User,Profile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

# admin.site.register(User)

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name','last_name','phone', 'last_login')}),
        ('Permissions', {'fields': (
            'is_active', 
            'is_staff', 
            'is_approved',
            'is_superuser',
            'groups', 
            'user_permissions',
        )}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2')
            }
        ),
    )
    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(UserAdmin, self).get_inline_instances(request, obj)


    list_display = ('email', 'first_name','last_name', 'phone','last_login')
    list_filter = ('is_staff', 'is_superuser', 'is_active','groups')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)


admin.site.register(User, UserAdmin)