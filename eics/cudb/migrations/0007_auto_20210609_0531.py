# Generated by Django 3.1.6 on 2021-06-09 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cudb', '0006_auto_20210605_0502'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket_task',
            name='cc_addresses',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='ticket_task',
            name='to_addresses',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
