# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-21 05:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operationlog',
            name='event_type',
            field=models.SmallIntegerField(choices=[(1, '执行命令'), (2, '分发文件'), (3, '服务部署'), (4, '用户管理'), (4, '部门管理')], verbose_name='操作类型'),
        ),
    ]