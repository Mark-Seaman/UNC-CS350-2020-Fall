# Generated by Django 3.0.8 on 2020-09-20 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_urlgame'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.CharField(max_length=100, null=True)),
                ('score', models.IntegerField(default=-1)),
                ('date', models.DateField(editable=False, null=True)),
                ('due', models.DateField(editable=False, null=True)),
                ('notes', models.TextField(null=True)),
                ('requirement_labels', models.TextField(default='NONE')),
                ('requirement_1', models.BooleanField(default=False)),
                ('requirement_2', models.BooleanField(default=False)),
                ('requirement_3', models.BooleanField(default=False)),
                ('requirement_4', models.BooleanField(default=False)),
                ('requirement_5', models.BooleanField(default=False)),
                ('requirement_6', models.BooleanField(default=False)),
                ('requirement_7', models.BooleanField(default=False)),
                ('requirement_8', models.BooleanField(default=False)),
                ('requirement_9', models.BooleanField(default=False)),
                ('requirement_10', models.BooleanField(default=False)),
                ('designer', models.ForeignKey(default=1, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='designer', to='course.UncStudent')),
                ('reviewer', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='course.UncStudent')),
            ],
        ),
    ]
