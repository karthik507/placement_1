# Generated by Django 3.2.10 on 2022-01-24 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TPO_app', '0008_auto_20220124_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventinfo',
            name='eventid',
            field=models.CharField(max_length=200),
        ),
    ]
