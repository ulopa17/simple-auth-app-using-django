# Generated by Django 3.2.7 on 2021-09-30 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210930_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='short_bio',
            field=models.TextField(blank=True, default='No bio..'),
        ),
    ]