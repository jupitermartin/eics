# Generated by Django 3.1.6 on 2021-06-04 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cudb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket_task',
            name='status',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]