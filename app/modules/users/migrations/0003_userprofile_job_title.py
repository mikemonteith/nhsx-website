# Generated by Django 3.0.4 on 2020-04-06 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='job_title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Job title'),
        ),
    ]
