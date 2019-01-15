# Generated by Django 2.1.3 on 2018-12-04 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SkateApp', '0004_userprofile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='../static/Imgs/Avatars'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(null=True, upload_to='../static/Imgs/Avatars'),
        ),
    ]