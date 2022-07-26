# Generated by Django 4.0.6 on 2022-07-20 10:57

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('text', models.TextField(default=True, max_length=1000, verbose_name='Positive')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('pub_date', models.DateTimeField(verbose_name='Date published')),
                ('change_date', models.DateTimeField(verbose_name='Date changed')),
                ('is_scum', models.BooleanField(default=False, verbose_name='Scum')),
            ],
            options={
                'verbose_name': 'Person',
                'verbose_name_plural': 'Persons',
                'ordering': ['-pub_date'],
            },
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name='Mark')),
                ('from_person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='from_person_mark', to='rating.person', verbose_name='From person')),
                ('to_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_person_mark', to='rating.person', verbose_name='To person')),
            ],
            options={
                'verbose_name': 'Mark',
                'verbose_name_plural': 'Marks',
            },
        ),
        migrations.CreateModel(
            name='CommentMark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_positive', models.BooleanField(verbose_name='Positive')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rating.comment', verbose_name='Comment')),
                ('from_person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rating.person', verbose_name='From person')),
            ],
            options={
                'verbose_name': 'CommentMark',
                'verbose_name_plural': 'CommentMarks',
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='from_person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='from_person_comment', to='rating.person', verbose_name='From person'),
        ),
        migrations.AddField(
            model_name='comment',
            name='to_person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_person_comment', to='rating.person', verbose_name='To person'),
        ),
    ]
