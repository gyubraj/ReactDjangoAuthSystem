# Generated by Django 2.2.7 on 2021-03-03 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20210303_1817'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='User',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='likes',
            old_name='User',
            new_name='user',
        ),
    ]
