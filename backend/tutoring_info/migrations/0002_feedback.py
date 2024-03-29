# Generated by Django 4.1.2 on 2022-10-14 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutoring_info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('version', models.PositiveSmallIntegerField(default=0, editable=False)),
                ('is_active', models.BooleanField(default=True)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
