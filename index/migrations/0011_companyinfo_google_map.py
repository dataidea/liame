# Generated by Django 4.2.6 on 2023-10-30 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0010_companyinfo_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyinfo',
            name='google_map',
            field=models.CharField(default='No google map', max_length=200),
        ),
    ]
