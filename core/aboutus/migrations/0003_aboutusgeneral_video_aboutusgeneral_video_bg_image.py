# Generated by Django 4.1.3 on 2023-01-02 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutus', '0002_alter_aboutusgeneral_text2'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutusgeneral',
            name='video',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='aboutusgeneral',
            name='video_bg_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]