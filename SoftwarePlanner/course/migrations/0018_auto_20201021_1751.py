# Generated by Django 3.1.2 on 2020-10-21 23:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0017_auto_20201010_1536'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='requirement_labels',
        ),
        migrations.AlterField(
            model_name='review',
            name='label_1',
            field=models.CharField(editable=False, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='label_10',
            field=models.CharField(editable=False, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='label_2',
            field=models.CharField(editable=False, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='label_3',
            field=models.CharField(editable=False, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='label_4',
            field=models.CharField(editable=False, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='label_5',
            field=models.CharField(editable=False, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='label_6',
            field=models.CharField(editable=False, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='label_7',
            field=models.CharField(editable=False, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='label_8',
            field=models.CharField(editable=False, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='label_9',
            field=models.CharField(editable=False, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='page',
            field=models.CharField(editable=False, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.IntegerField(default=-1, editable=False),
        ),
        migrations.CreateModel(
            name='ZoomLecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zoom_url', models.URLField()),
                ('lesson', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='course.lesson')),
            ],
        ),
    ]