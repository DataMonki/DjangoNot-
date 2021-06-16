from django.contrib import admin
from . import models


# Apply summernote to all TextField in model.4
@admin.register(models.Gallery)
class GalleryAdmin(admin.ModelAdmin):  # instead of ModelAdmin
    prepopulated_fields = {'slug': ('title',), } #this means that when title is entered the url