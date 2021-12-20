from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from autoslug import AutoSlugField
from datetime import date
import datetime
from django.utils.text import slugify
from .utils import create_event


STATUS = (
    ('Draft','Draft'),
    ('Published','Published'),
)

THEME = (
    ('Light','Light'),
    ('Dark','Dark'),
)
class EventType(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category

class Events(models.Model):
    title = models.CharField(max_length = 200)
    title_slug = AutoSlugField(populate_from = 'title',unique = True,editable = True)
    start_date = models.DateTimeField(blank = True,null = True)
    end_date = models.DateTimeField(blank = True,null = True)
    description = models.TextField(blank = True,null = True)
    truncated_description = models.BooleanField(default=False)
    agenda = models.TextField(blank = True,null = True)
    status = models.CharField(choices = STATUS, max_length = 10,default = 'Draft')
    event_type = models.ForeignKey(EventType, null=True, on_delete=models.SET_NULL)
    email_confirmation = models.TextField(blank = True,null = True)
    created_on = models.DateField(blank = True,null = True,default = datetime.date.today)
    registration = models.CharField(max_length = 200,blank=True)
    icon = models.ImageField(blank= True, null = True, help_text="Resolution 84 * 84")
    banner = models.ImageField(blank= True, null = True, help_text="Resolution 1500 * 300")
    banner_color = models.CharField(choices = THEME, max_length = 10,default = 'Light')
    keywords = models.TextField(default = 'Event')
    open_graph_banner = models.ImageField(blank= True, null = True,)
    def save(self, *args, **kwargs):
        #self.title_slug = slugify(kwargs.pop('title', self.title))
        #create_event(self.title, self.start_date, self.end_date,self.description)
        super(Events, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"
        ordering = ['-end_date']
    def update_registration(self):
        if date.today() <= self.end_date.date():
            self.registration = "Registrations Open"
        else:
            self.registration = "Registrations Closed"
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('event_detail', args=[self.title_slug])



