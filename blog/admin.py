from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin
from django import forms

class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].required = True

    class Meta:
        model = Post
        fields = '__all__'

class blogadmin(SummernoteModelAdmin):
    list_display = ('title', 'title_slug', 'status', 'created_on','image')
    summernote_fields = ('body', )
    form = PostForm

admin.site.register(Post, blogadmin)


