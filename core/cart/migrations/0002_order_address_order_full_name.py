# Generated by Django 4.1.3 on 2023-01-14 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='full_name',
            field=models.CharField(max_length=250, null=True),
        ),
    ]