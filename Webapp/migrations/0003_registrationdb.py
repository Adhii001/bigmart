# Generated by Django 5.0.4 on 2024-05-28 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webapp', '0002_alter_contactinfodb_cmessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='registrationdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Email', models.CharField(blank=True, max_length=100, null=True)),
                ('Password', models.CharField(blank=True, max_length=500, null=True)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='CS_Image')),
            ],
        ),
    ]
