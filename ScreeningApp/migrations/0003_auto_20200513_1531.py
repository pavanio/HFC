# Generated by Django 2.2.4 on 2020-05-13 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ScreeningApp', '0002_auto_20200429_1301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expertise_area',
            name='category_of_expertise',
        ),
        migrations.AddField(
            model_name='question',
            name='level',
            field=models.CharField(choices=[('Entry Level', 'Entry Level'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced'), ('Expert', 'Expert')], default='Entry Level', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='topic',
            field=models.CharField(default='ORM', max_length=200),
            preserve_default=False,
        ),
    ]