# Generated by Django 3.2.4 on 2021-06-16 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='img',
            field=models.ImageField(upload_to='articles/'),
        ),
    ]
