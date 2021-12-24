# Generated by Django 3.2 on 2021-12-22 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HFCCore', '0044_alter_community_member_years_of_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_partner',
            name='project_involvement',
            field=models.CharField(choices=[('Funding', 'Funding'), ('Execution', 'Execution'), ('Adoption', 'Adoption'), ('Promotion', 'Promotion')], max_length=50, verbose_name='Partnership'),
        ),
    ]