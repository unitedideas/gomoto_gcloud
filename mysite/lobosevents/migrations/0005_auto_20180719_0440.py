# Generated by Django 2.0.5 on 2018-07-19 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lobosevents', '0004_auto_20180719_0439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_name',
            field=models.TimeField(blank=True, max_length=300, null=True),
        ),
    ]
