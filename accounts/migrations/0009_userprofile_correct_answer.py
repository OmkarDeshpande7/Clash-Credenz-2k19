# Generated by Django 2.0.7 on 2018-09-06 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20180905_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='correct_answer',
            field=models.IntegerField(default=0),
        ),
    ]
