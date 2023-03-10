# Generated by Django 4.1.3 on 2023-01-19 10:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUsGeneral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1', models.CharField(max_length=155)),
                ('title2', models.CharField(max_length=155)),
                ('title3', models.CharField(max_length=155)),
                ('text1', models.TextField()),
                ('text2', models.TextField()),
                ('text3', models.TextField()),
                ('video', models.FileField(null=True, upload_to='')),
                ('video_bg_image', models.ImageField(null=True, upload_to='')),
                ('image1', models.ImageField(upload_to='')),
                ('alt1', models.CharField(max_length=50)),
                ('image2', models.ImageField(upload_to='')),
                ('alt2', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='AboutUsProgressBar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155)),
                ('percentage', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='AboutUsProperty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155)),
                ('text', models.TextField()),
            ],
        ),
    ]
