# Generated by Django 5.0.7 on 2024-08-03 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distributions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apk',
            name='apk_path',
        ),
        migrations.AddField(
            model_name='apk',
            name='apk_file',
            field=models.FileField(default=23, upload_to='apks/'),
            preserve_default=False,
        ),
    ]
