# Generated by Django 5.0.4 on 2024-06-02 11:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_alter_userprofile_bio_alter_userprofile_nama_lengkap'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='topic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.topics'),
        ),
    ]
