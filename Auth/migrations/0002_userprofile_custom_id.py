# Generated by Django 5.0.7 on 2024-07-11 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='custom_id',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]
