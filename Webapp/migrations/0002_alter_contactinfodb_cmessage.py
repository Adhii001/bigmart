# Generated by Django 5.0.4 on 2024-05-11 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinfodb',
            name='cmessage',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
