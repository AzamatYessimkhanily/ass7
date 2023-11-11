from django.contrib import admin
from .models import Clothing, Shoes,Аccessories


class ClothingAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    ordering = ('name', )
    search_fields = ('name',)
    list_filter = ('size', 'color')



admin.site.register(Shoes)
admin.site.register(Аccessories)
admin.site.register(Clothing, ClothingAdmin,)

