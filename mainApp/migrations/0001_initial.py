# Generated by Django 3.2.6 on 2021-08-22 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.IntegerField()),
                ('user_ids', models.CharField(max_length=1000)),
                ('chat_photo', models.ImageField(upload_to='photos/chat_photos')),
                ('msg_history', models.CharField(max_length=1000000)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator_id', models.IntegerField()),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('photos', models.ImageField(upload_to='photos/post_photos')),
                ('text', models.CharField(max_length=1000)),
                ('like_num', models.IntegerField()),
                ('like_list', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=300)),
                ('profile_photo', models.ImageField(upload_to='photos/profile_photos')),
            ],
        ),
    ]