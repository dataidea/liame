# Generated by Django 4.2.6 on 2023-10-30 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_blogpage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_featured',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
