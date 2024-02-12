from django.contrib import admin
from .models import *


# class PostAdmin(admin.ModelAdmin):
#     list_display = ['id','title','date']
#     list_display_links = ['id','title']
#     search_fields = ['id','title']
#     ordering = ['-id']
# # Register your models here.
# admin.site.register(Post,PostAdmin)
admin.site.register(ToDo)