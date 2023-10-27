# Generated by Django 4.2.6 on 2023-10-26 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('subject', models.CharField(max_length=244)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FrequentlyAskedQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=122)),
                ('answer', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PrivacyPolicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Privacy Policy', max_length=122)),
                ('description', models.TextField(default='By using the services provided by Data Idea ("the Company"), you agree to comply with and be bound by the following Privacy Policy ("Privacy Policy"). If you do not agree with these terms, please do not use our services.')),
            ],
        ),
        migrations.CreateModel(
            name='TermOfService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Terms of Service', max_length=122)),
                ('description', models.TextField(default='By using the services provided by Data Idea ("the Company"), you agree to comply with and be bound by the following Terms of Service ("TOS"). If you do not agree with these terms, please do not use our services.')),
            ],
        ),
    ]
