# Generated by Django 4.2 on 2023-05-02 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreateBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('intro', models.TextField()),
                ('auteur', models.TextField()),
                ('body', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-date_update'],
            },
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('name', models.CharField(default='marie', max_length=200)),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='store.createblog')),
            ],
            options={
                'ordering': ['-date_update'],
            },
        ),
    ]