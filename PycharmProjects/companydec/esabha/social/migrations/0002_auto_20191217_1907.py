# Generated by Django 2.2.5 on 2019-12-17 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postcomments',
            old_name='comments',
            new_name='commented_by',
        ),
    ]
