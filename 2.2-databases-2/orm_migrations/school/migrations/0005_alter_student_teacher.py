# Generated by Django 4.2.4 on 2023-08-09 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_alter_student_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='teacher',
            field=models.ManyToManyField(related_name='students', to='school.teacher'),
        ),
    ]
