# Generated by Django 3.2 on 2022-01-28 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventsEngine', '0015_event_speakers'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='total_seat',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
