from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin

class blogadmin(SummernoteModelAdmin):
    list_display = ('title', 'title_slug', 'status', 'created_on','image')
    summernote_fields = ('body', )

admin.site.register(Post, blogadmin)
