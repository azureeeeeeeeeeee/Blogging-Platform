# Generated by Django 5.0.4 on 2024-05-26 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_news_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='thumbnail',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
