# Generated by Django 4.1.2 on 2022-11-13 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_profile_avatar_url_alter_profile_department_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='introduction',
            field=models.TextField(blank=True, null=True, verbose_name='Introduce (about me) (optional)'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar_url',
            field=models.URLField(null=True, verbose_name='Avatar URL (optional)'),
        ),
    ]
