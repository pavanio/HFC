# Generated by Django 3.2.4 on 2021-11-25 14:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventsEngine', '0011_rename_truncated_descripton_events_truncated_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='created_on',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
    ]
