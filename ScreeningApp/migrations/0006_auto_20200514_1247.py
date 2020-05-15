# Generated by Django 2.2.4 on 2020-05-14 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ScreeningApp', '0005_auto_20200513_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='contact_number',
            field=models.CharField(default='None', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidate',
            name='dob',
            field=models.DateField(default='2020-05-14'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidate',
            name='highest_education',
            field=models.CharField(choices=[('Intermediate', 'Intermediate'), ('Bachelors', 'Bachelors'), ('Masters', 'Masters')], default='Bachelors', max_length=50),
            preserve_default=False,
        ),
    ]