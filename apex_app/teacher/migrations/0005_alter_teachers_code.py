# Generated by Django 5.0.6 on 2024-07-07 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0004_remove_teachers_id_remove_teachers_teacher_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachers',
            name='code',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
