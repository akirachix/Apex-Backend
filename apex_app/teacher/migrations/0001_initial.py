# Generated by Django 5.0.6 on 2024-07-06 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('school_code', models.PositiveSmallIntegerField()),
                ('course_id', models.PositiveSmallIntegerField()),
                ('password', models.CharField(max_length=20)),
                ('user_name', models.CharField(max_length=20)),
            ],
        ),
    ]