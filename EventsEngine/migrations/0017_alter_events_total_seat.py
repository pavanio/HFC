# Generated by Django 3.2 on 2022-01-29 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventsEngine', '0016_events_total_seat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='total_seat',
            field=models.CharField(blank=True, default=100, max_length=10, null=True),
        ),
    ]
