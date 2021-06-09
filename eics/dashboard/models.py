from django.db import models

# Create your models here.

class MaintTickets(models.Model):
    maint_ticketsid = models.CharField(db_column='maint_ticketsID', primary_key=True, max_length=15)  # Field name made lowercase.
    maint_tickets_task = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'maint_tickets'


class Ribbon(models.Model):
    ribbonid = models.AutoField(db_column='ribbonID', primary_key=True)  # Field name made lowercase.
    fibrenolow = models.IntegerField(db_column='fibreNoLow', blank=True, null=True)  # Field name made lowercase.
    fibrenohigh = models.IntegerField(db_column='fibreNoHigh', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ribbon'


class RibbonToFibre(models.Model):
    ribbon_to_fibreid = models.AutoField(db_column='ribbon_to_fibreID', primary_key=True)  # Field name made lowercase.
    ribbonid = models.ForeignKey(Ribbon, models.DO_NOTHING, db_column='ribbonID')  # Field name made lowercase.
    fibre = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'ribbon_to_fibre'


class SplicePointData(models.Model):
    section = models.IntegerField(db_column='Section', blank=True, null=True)  # Field name made lowercase.
    splice_pt = models.TextField(db_column='Splice Pt', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    step_chamber_id = models.TextField(db_column='Step Chamber ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    address = models.TextField(db_column='Address', blank=True, null=True)  # Field name made lowercase.
    north = models.TextField(blank=True, null=True)
    west = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'splice_point_data'


class SpliceToFibre(models.Model):
    splice_to_fibreid = models.AutoField(db_column='splice_to_fibreID', primary_key=True)  # Field name made lowercase.
    splice = models.CharField(max_length=45)
    fibre = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'splice_to_fibre'