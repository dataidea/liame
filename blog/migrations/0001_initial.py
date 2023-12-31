# Generated by Django 4.2.6 on 2023-10-26 08:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='dataidea', max_length=122)),
                ('email', models.CharField(default='datasideaofficial@gmail.com', max_length=122)),
                ('profile', models.CharField(default='No profile provided', max_length=122)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(default='New Blog Slug', max_length=122)),
                ('title', models.CharField(max_length=122)),
                ('brief', models.TextField(default='')),
                ('cover_image', models.CharField(default='no image', max_length=122)),
                ('popularity', models.FloatField(default=0)),
                ('date_featured', models.CharField(default='no date', max_length=122, null=True)),
                ('content_markdown', models.TextField(default='')),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.author')),
            ],
        ),
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='New category', max_length=122)),
                ('description', models.CharField(default='New category description', max_length=122)),
                ('color', models.CharField(default='purple', max_length=122)),
            ],
        ),
        migrations.CreateModel(
            name='BlogComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approved', models.BooleanField(default=False)),
                ('comment', models.TextField(default='New Comment')),
                ('blog', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='blog.blog')),
                ('user', models.ForeignKey(default=12, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.blogcategory'),
        ),
    ]
