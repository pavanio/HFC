# Generated by Django 2.2.4 on 2020-04-10 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ScreeningApp', '0002_auto_20200410_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='screening',
            name='question_id',
            field=models.ManyToManyField(to='ScreeningApp.Question'),
        ),
    ]
