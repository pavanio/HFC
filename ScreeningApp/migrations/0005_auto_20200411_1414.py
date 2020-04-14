# Generated by Django 2.2.4 on 2020-04-11 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ScreeningApp', '0004_auto_20200411_1336'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate_Screening',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('screening_uuid', models.CharField(max_length=200)),
                ('candidate_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ScreeningApp.Candidate')),
                ('screening_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ScreeningApp.Screening_Question')),
            ],
        ),
        migrations.DeleteModel(
            name='Candidates_Screening',
        ),
    ]
