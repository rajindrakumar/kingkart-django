from django.contrib import admin
from .models import Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    # This is the code for prepopulatd slug 
    prepopulated_fields = {'slug': ('category_name',)}

    # To display the table 
    list_display  = ('category_name','slug')

admin.site.register(Category,CategoryAdmin)