# Generated by Django 5.0.6 on 2024-05-20 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_question_choice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='body',
        ),
    ]
