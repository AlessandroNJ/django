# Generated by Django 4.2.7 on 2023-11-23 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='logmessage',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
