# Generated by Django 3.2 on 2021-12-11 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventsEngine', '0012_events_created_on'),
        ('HFCCore', '0042_alter_problem_statement_organisation'),
    ]

    operations = [
        migrations.AddField(
            model_name='community_member',
            name='event',
            field=models.ManyToManyField(blank=True, null=True, to='EventsEngine.Events'),
        ),
    ]
