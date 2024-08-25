# Generated by Django 4.2.15 on 2024-08-24 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='section',
            field=models.CharField(choices=[('A', 'Section A'), ('B', 'Section B'), ('C', 'Section C'), ('D', 'Section D'), ('E', 'Section E')], default='A', max_length=1),
        ),
    ]
