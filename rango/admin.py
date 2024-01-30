from django.contrib import admin
from rango.models import Category, Page
# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ('category','title','url')

class CategoryAdmin(admin.ModelAdmin):
    propulated_fields = {'slug':('name',)}
    
admin.site.register(Category,CategoryAdmin)
admin.site.register(Page,PageAdmin)