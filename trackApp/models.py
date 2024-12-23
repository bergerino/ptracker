# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Daytotaluser(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    userid = models.IntegerField(blank=False, null=False, primary_key=True)
    spent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    date_spent = models.TextField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'daytotaluser'


class Issueperdayuser(models.Model):
    project = models.CharField(max_length=255, blank=True, null=True)
    projectid = models.IntegerField(blank=True, null=True)
    issue = models.CharField(max_length=255, blank=True, null=True)
    issueid = models.IntegerField(blank=False, null=False, primary_key=True)
    userid = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    spent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    date_spent = models.TextField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'issueperdayuser'


class Issuetotaluser(models.Model):
    issue = models.CharField(max_length=255, blank=True, null=True)
    issueid = models.IntegerField(blank=False, null=False, primary_key=True)
    project = models.CharField(max_length=255, blank=True, null=True)
    projectid = models.IntegerField(blank=True, null=True)
    userid = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    spent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'issuetotaluser'


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
    user_id = models.IntegerField(blank=False, null=False, primary_key=True)
    name_id = models.CharField(max_length=255, blank=True, null=True)
    all_spent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    request = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    bug = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    operational = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    meeting = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    absence = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'userspent'


class Userspentonprojects(models.Model):
    issueid = models.IntegerField(blank=True, null=True)
    projectid = models.IntegerField(blank=True, null=True)
    userid = models.IntegerField(blank=False, null=False, primary_key=True)
    project = models.CharField(max_length=255, blank=True, null=True)
    issue = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    spent = models.TextField(blank=True, null=True)
    date_spent = models.DateTimeField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'userspentonprojects'
