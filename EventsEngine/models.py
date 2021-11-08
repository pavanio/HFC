from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from autoslug import AutoSlugField
from datetime import date
import datetime


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
    title_slug = AutoSlugField(populate_from = 'title')
    start_date = models.DateTimeField(blank = True,null = True)
    end_date = models.DateTimeField(blank = True,null = True)
    description = models.TextField(blank = True,null = True)
    agenda = models.TextField(blank = True,null = True)
    status = models.CharField(choices = STATUS, max_length = 10,default = 'Draft')
    event_type = models.ForeignKey(EventType, null=True, on_delete=models.SET_NULL)
    email_confirmation = models.TextField(blank = True,null = True)
    registration = models.CharField(max_length = 200,blank=True)
    logo = models.ImageField(blank= True, null = True)
    banner = models.ImageField(blank= True, null = True)
    banner_color = models.CharField(choices = THEME, max_length = 10,default = 'Light')

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



