# Generated by Django 4.2 on 2023-05-10 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_createblog_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='createblog',
            old_name='date',
            new_name='pub_date',
        ),
    ]
