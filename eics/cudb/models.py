from django.db import models

# Create your models here.

class Ticket_task(models.Model):
    ticketid = models.CharField(primary_key=True, unique=True, max_length=255)
    reason = models.CharField(blank=True, max_length=255)
    priority = models.CharField(max_length=4)
    start_date = models.DateTimeField(blank=True, max_length=255)
    end_date = models.DateTimeField(blank=True, max_length=255, null=True, default=None)
    duration = models.IntegerField(default=0)
    splice_num = models.CharField(blank=True, max_length=255)
    location = models.CharField(blank=True, max_length=255)
    north = models.CharField(blank=True, max_length=255)
    west = models.CharField(blank=True, max_length=255)
    circuits = models.TextField(blank=True)
    email_sent = models.BooleanField(default=False)
    status = models.IntegerField(default=0)
    to_addresses = models.CharField(blank=True, max_length=255)
    cc_addresses = models.CharField(blank=True, max_length=255)