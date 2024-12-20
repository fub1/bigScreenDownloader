# Generated by Django 5.0.7 on 2024-08-03 05:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name': '客户端', 'verbose_name_plural': '客户端'},
        ),
        migrations.AlterModelOptions(
            name='clientlog',
            options={'verbose_name': '客户端日志', 'verbose_name_plural': '客户端日志'},
        ),
        migrations.AlterField(
            model_name='client',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='客户端注册日期'),
        ),
        migrations.AlterField(
            model_name='client',
            name='identifier',
            field=models.CharField(max_length=255, verbose_name='客户端识别代码'),
        ),
        migrations.AlterField(
            model_name='client',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='客户端关闭'),
        ),
        migrations.AlterField(
            model_name='clientlog',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='clients.client', verbose_name='客户端识别代码'),
        ),
        migrations.AlterField(
            model_name='clientlog',
            name='ip',
            field=models.CharField(max_length=15, verbose_name='客户端ip地址'),
        ),
        migrations.AlterField(
            model_name='clientlog',
            name='logged_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='在线日期'),
        ),
    ]
