# Generated by Django 5.0.6 on 2024-05-31 09:44

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_anotherpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='anotherpage',
            name='intro',
            field=wagtail.fields.RichTextField(blank=True),
        ),
    ]
