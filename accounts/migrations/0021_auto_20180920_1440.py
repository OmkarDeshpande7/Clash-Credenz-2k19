# Generated by Django 2.0.7 on 2018-09-20 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_auto_20180920_0642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mcq',
            name='A',
            field=models.TextField(default=' ', max_length=150),
        ),
        migrations.AlterField(
            model_name='mcq',
            name='B',
            field=models.TextField(default=' ', max_length=150),
        ),
        migrations.AlterField(
            model_name='mcq',
            name='C',
            field=models.TextField(default=' ', max_length=150),
        ),
        migrations.AlterField(
            model_name='mcq',
            name='D',
            field=models.TextField(default=' ', max_length=150),
        ),
    ]