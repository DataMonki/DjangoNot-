from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from . import models


#class ArticleAdmin(admin.ModelAdmin):
    


# Apply summernote to all TextField in model.4
@admin.register(models.Articles)
class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    prepopulated_fields = {'slug': ('title',), } #this means that when title is entered the url 


#admin.site.register(models.Articles, SomeModelAdmin)    