# Generated by Django 3.0.4 on 2020-03-06 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_scrap', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='toolkit',
            name='content',
            field=models.TextField(blank=True),
        ),
    ]
