# Generated by Django 3.2.8 on 2021-10-15 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20211015_1236'),
    ]

    operations = [
        migrations.RenameField(
            model_name='campus',
            old_name='ints_count',
            new_name='inst_count',
        ),
    ]
