# Generated by Django 4.2.15 on 2024-08-25 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_alter_student_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='roll_no',
            field=models.IntegerField(default=5000, editable=False, unique=True),
        ),
    ]
