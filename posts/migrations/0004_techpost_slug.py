# Generated by Django 3.1.5 on 2021-03-07 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20210307_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='techpost',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
