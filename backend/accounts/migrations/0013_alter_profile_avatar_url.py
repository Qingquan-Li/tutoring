# Generated by Django 4.1.2 on 2023-02-08 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_alter_profile_avatar_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar_url',
            field=models.URLField(null=True, verbose_name='Avatar URL (optional)'),
        ),
    ]
