# Generated by Django 2.2 on 2019-08-03 23:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20190804_0125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comment_count',
        ),
    ]
