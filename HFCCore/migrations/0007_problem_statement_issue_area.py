# Generated by Django 2.2.4 on 2020-06-15 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HFCCore', '0006_community_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem_statement',
            name='issue_area',
            field=models.CharField(default='Community', max_length=100),
            preserve_default=False,
        ),
    ]
