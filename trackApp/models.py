# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Projectspent(models.Model):
    projectid = models.IntegerField(blank=False, null=False, primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    creator = models.CharField(max_length=255, blank=True, null=True)
    spent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    spent_txt = models.TextField(blank=True, null=True)
    date_spent = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'projectspent'

class Userspent(models.Model):
    userid = models.IntegerField(blank=False, null=False, primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    spent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    spent_txt = models.TextField(blank=True, null=True)
    date_spent = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'userspent'


class Userspentonprojects(models.Model):
    issueid = models.IntegerField(blank=False, null=False, primary_key=True)
    projectid = models.IntegerField(blank=True, null=True)
    userid = models.IntegerField(blank=True, null=True)
    project = models.CharField(max_length=255, blank=True, null=True)
    issue = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    spent = models.TextField(blank=True, null=True)
    date_spent = models.DateTimeField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'userspentonprojects'
