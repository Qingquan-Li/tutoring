# Generated by Django 4.1.2 on 2022-10-14 01:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_remove_department_institution'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar_url',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.department'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='institution',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.institution'),
        ),
    ]