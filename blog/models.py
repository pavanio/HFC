from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from autoslug import AutoSlugField
import datetime

STATUS = (
    ('Draft','Draft'),
    ('Published','Published'),
)

class Post(models.Model):
    title = models.CharField(max_length = 100)
    title_slug = AutoSlugField(populate_from = 'title')
    body = models.TextField()
    author = models.ForeignKey(User, null = True, on_delete = models.SET_NULL)
    image = models.ImageField(null=True, blank=True)
    created_on = models.DateField(blank = True,null = True,default = datetime.date.today)
    status = models.CharField(choices = STATUS, max_length = 10,default = 'Draft')
    keyword = models.TextField()
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['-created_on']
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog-detail', args=[self.title_slug])
