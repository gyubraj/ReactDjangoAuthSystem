# Generated by Django 2.2.7 on 2021-02-24 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_useraccount_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
