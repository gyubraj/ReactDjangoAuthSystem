# Generated by Django 2.2.7 on 2021-03-03 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20210302_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='deactivate',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
