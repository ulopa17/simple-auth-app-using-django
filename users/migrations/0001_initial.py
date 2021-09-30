# Generated by Django 3.2.7 on 2021-09-29 07:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=255)),
                ('profile_pic', models.ImageField(blank=True, default='profiles/default.jpg', upload_to='profiles/')),
                ('country', models.CharField(blank=True, default='No Country', max_length=200)),
                ('social_twitter', models.CharField(blank=True, default='twitter.com', max_length=250)),
                ('social_linkedin', models.CharField(blank=True, default='linkedin.com', max_length=250)),
                ('social_facebook', models.CharField(blank=True, default='facebook.com.com', max_length=250)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]