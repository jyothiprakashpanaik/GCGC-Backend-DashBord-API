# Generated by Django 3.2.8 on 2021-12-25 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_courses'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='is_ug',
            field=models.BooleanField(default=True),
        ),
    ]
