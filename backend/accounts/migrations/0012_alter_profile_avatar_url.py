# Generated by Django 4.1.2 on 2023-02-08 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_alter_customuser_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar_url',
            field=models.URLField(default='https://helpyourmath.com/images/img/logo1.jpg', verbose_name='Avatar URL'),
            preserve_default=False,
        ),
    ]
