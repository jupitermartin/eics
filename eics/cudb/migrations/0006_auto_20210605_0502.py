# Generated by Django 3.1.6 on 2021-06-05 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cudb', '0005_auto_20210605_0459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket_task',
            name='end_date',
            field=models.DateTimeField(blank=True, default=None, max_length=255, null=True),
        ),
    ]
