# Generated by Django 4.2.6 on 2023-10-26 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_delete_quotation_companyinfo_quote_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='exhibition',
            name='category',
            field=models.CharField(default='Category', max_length=50),
        ),
    ]
