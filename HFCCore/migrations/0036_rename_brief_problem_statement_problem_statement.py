# Generated by Django 3.2 on 2021-07-28 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HFCCore', '0035_community_organization_is_public'),
    ]

    operations = [
        migrations.RenameField(
            model_name='problem_statement',
            old_name='brief',
            new_name='problem_statement',
        ),
    ]
