# Generated by Django 4.2.4 on 2023-08-09 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_remove_student_teacher_student_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='teacher',
            field=models.ManyToManyField(to='school.teacher'),
        ),
    ]
