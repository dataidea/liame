# Generated by Django 4.2.6 on 2023-10-30 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0008_companyinfo_logo_alter_partner_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyinfo',
            name='support_email',
            field=models.CharField(default='XXXXXXXXXXXXXXXXXXXXXXXX', max_length=50),
        ),
        migrations.AddField(
            model_name='companyinfo',
            name='telephone',
            field=models.CharField(default='000000000000', max_length=50),
        ),
    ]
