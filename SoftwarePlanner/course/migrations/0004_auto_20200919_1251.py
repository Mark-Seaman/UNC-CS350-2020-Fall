# Generated by Django 3.0.8 on 2020-09-19 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_appteam_teammember'),
    ]

    operations = [
        migrations.AddField(
            model_name='appteam',
            name='github',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='appteam',
            name='server',
            field=models.CharField(max_length=100, null=True),
        ),
    ]