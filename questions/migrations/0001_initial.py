# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-04 18:09
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b"Answer's Date")),
                ('text', models.TextField(verbose_name=b"Answer's Content")),
                ('rating', models.IntegerField(default=0, verbose_name=b"Answer's Rating")),
            ],
        ),
        migrations.CreateModel(
            name='LikeDislike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.SmallIntegerField(choices=[(-1, b'Dislike'), (1, b'Like')], verbose_name=b'Vote')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name=b"Question's Header")),
                ('text', models.TextField(verbose_name=b"Question's Content")),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b"Question's Date")),
                ('rating', models.IntegerField(default=0, verbose_name=b"Question's Rating")),
                ('is_active', models.BooleanField(default=True, verbose_name=b"Question's Availability")),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=b'404', max_length=20, verbose_name=b"Question's Tag")),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('upload', models.ImageField(default=b'default/default_avatar.png', upload_to=b'uploads/%Y/%m/%d/', verbose_name=b"User's Avatar")),
                ('registration_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b"User's Registration Date")),
                ('rating', models.IntegerField(default=0, verbose_name=b"User's Rating")),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.User', verbose_name=b"Question's Owner"),
        ),
        migrations.AddField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(default=True, related_name='questions', to='questions.Tag', verbose_name=b"Question's Tags"),
        ),
        migrations.AddField(
            model_name='likedislike',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.User', verbose_name=b'User'),
        ),
        migrations.AddField(
            model_name='answer',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.User', verbose_name=b"Answer's Owner"),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='questions.Question', verbose_name=b"Answer's Question"),
        ),
    ]
