# Generated by Django 2.0.7 on 2018-09-05 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mcq',
            name='level',
            field=models.IntegerField(default=0),
        ),
    ]
