# Generated by Django 5.0.4 on 2024-05-31 15:13

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_news_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]