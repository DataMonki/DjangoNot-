from django.contrib import admin
from . import models


@admin.register(models.Articles)
class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',), } #this means that when title is entered the url 
