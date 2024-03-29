from django.contrib import admin
from .models import Account
#to do password non editable
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class AccountAdmin(UserAdmin):
    # The data to show as table in account>user section 
    list_display = ('email','first_name','last_name','username','last_login','date_joined','is_active')
    # the table which is for getinside the user data 
    list_display_links = ('email','first_name','last_name')
    # the table which is for readonly 
    readonly_fields = ('last_login','date_joined')
    # to make order in horizontal order 
    ordering = ('-date_joined',)

    # to show user list horizontally
    filter_horizontal = ()
    list_filter = ()
    # this will  make password readonly 
    fieldsets = ()

admin.site.register(Account, AccountAdmin)
