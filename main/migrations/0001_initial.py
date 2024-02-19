# Generated by Django 5.0.1 on 2024-02-03 17:45

import ckeditor_uploader.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='carousel/')),
                ('color', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='courses/')),
                ('title', models.CharField(max_length=100)),
                ('marketing_line', models.CharField(max_length=1000)),
                ('description_for_card', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='enroll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('gurdian_name', models.CharField(max_length=100)),
                ('gurdian_phone', models.IntegerField()),
                ('gurdian_relation', models.CharField(max_length=100)),
                ('courses', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='gallery/')),
            ],
        ),
        migrations.CreateModel(
            name='give_number',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('date_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='notices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='class_topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('courses', models.ManyToManyField(to='main.courses', verbose_name='Courses')),
            ],
        ),
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='profile/default.png', upload_to='profile/')),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('result', models.FileField(default='results/default.pdf', upload_to='results/')),
                ('courses', models.ManyToManyField(to='main.courses', verbose_name='Courses')),
            ],
        ),
        migrations.CreateModel(
            name='routine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('routine_pdf', models.FileField(default='routine/nonepdf.pdf', upload_to='routine/')),
                ('courses', models.ManyToManyField(to='main.courses', verbose_name='Courses')),
            ],
        ),
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='students/')),
                ('address', models.CharField(max_length=100)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('courses', models.ManyToManyField(to='main.courses', verbose_name='Courses')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='main.profile')),
            ],
        ),
        migrations.CreateModel(
            name='student_payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_for', models.CharField(max_length=100)),
                ('paid_amount', models.IntegerField()),
                ('paid_date', models.DateField()),
                ('name', models.ManyToManyField(to='main.students', verbose_name='Students')),
            ],
        ),
        migrations.CreateModel(
            name='students_attandance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('name', models.ManyToManyField(to='main.students', verbose_name='Students')),
            ],
        ),
        migrations.CreateModel(
            name='teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='students/')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('salary', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teachers', to='main.profile')),
            ],
        ),
        migrations.CreateModel(
            name='teachers_attandance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('name', models.ManyToManyField(to='main.teachers', verbose_name='Teachers')),
            ],
        ),
    ]