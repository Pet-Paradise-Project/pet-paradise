# Generated by Django 3.2.5 on 2021-10-07 18:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='petOwner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yourname', models.CharField(default='', max_length=255)),
                ('ownerImage', models.ImageField(default='Images/user_profile1.png', null=True, upload_to='Images/')),
                ('contact', models.CharField(default='', max_length=13)),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(default='', max_length=255)),
                ('user', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='petDoctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yourname', models.CharField(default='', max_length=255)),
                ('doctorImage', models.ImageField(default='Images/user_profile1.png', null=True, upload_to='Images/')),
                ('contact', models.CharField(default='', max_length=13)),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(default='', max_length=255)),
                ('user', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
