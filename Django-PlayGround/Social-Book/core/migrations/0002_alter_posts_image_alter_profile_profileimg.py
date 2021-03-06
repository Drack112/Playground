# Generated by Django 4.0.5 on 2022-07-02 23:05

import cloudinary_storage.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='image',
            field=models.ImageField(storage=cloudinary_storage.storage.MediaCloudinaryStorage(), upload_to='post_images'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profileimg',
            field=models.ImageField(default='blank-profile-picture.png', storage=cloudinary_storage.storage.MediaCloudinaryStorage(), upload_to='profile_images'),
        ),
    ]
