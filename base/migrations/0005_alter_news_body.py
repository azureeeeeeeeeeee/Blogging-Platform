# Generated by Django 5.0.4 on 2024-05-31 11:11

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_news_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
    ]