# Generated by Django 5.0.4 on 2024-05-04 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categorydb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(blank=True, max_length=100, null=True)),
                ('cdescription', models.CharField(blank=True, max_length=500, null=True)),
                ('cimage', models.ImageField(blank=True, null=True, upload_to='product_images')),
            ],
        ),
    ]
