# Generated by Django 3.0.6 on 2020-05-08 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HFCCore', '0004_delete_organization'),
    ]

    operations = [
        migrations.CreateModel(
            name='Community_Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization_name', models.CharField(max_length=500)),
                ('type', models.CharField(choices=[('Center', 'Center'), ('Chapter', 'Chapter')], max_length=100)),
                ('website', models.URLField(blank=True, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='')),
                ('coordinator_name', models.CharField(max_length=100)),
                ('coordinator_email', models.EmailField(max_length=254)),
                ('coordinator_mobile', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Community_Organization',
                'verbose_name_plural': 'Community_Organizations',
            },
        ),
    ]
