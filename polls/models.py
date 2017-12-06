# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Friend(models.Model):
    userid1 = models.IntegerField(db_column='userID1', primary_key=True)  # Field name made lowercase.
    userid2 = models.IntegerField(db_column='userID2')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'friend'
        unique_together = (('userid1', 'userid2'),)


class Movies(models.Model):
    movieid = models.IntegerField(db_column='movieID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=100)  # Field name made lowercase.
    genre = models.CharField(db_column='Genre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    director = models.CharField(db_column='Director', max_length=50, blank=True, null=True)  # Field name made lowercase.
    actors = models.CharField(db_column='Actors', max_length=200, blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    runtime = models.IntegerField(db_column='RunTime', blank=True, null=True)  # Field name made lowercase.
    votes = models.IntegerField(db_column='Votes', blank=True, null=True)  # Field name made lowercase.
    revenue = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movies'


class Users(models.Model):
    userid = models.IntegerField(db_column='userID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='userName', max_length=20)  # Field name made lowercase.
    password = models.CharField(max_length=20)
    location = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class Watched(models.Model):
    userid = models.IntegerField(db_column='userID', primary_key=True)  # Field name made lowercase.
    movieid = models.IntegerField(db_column='movieID')  # Field name made lowercase.
    rating = models.FloatField(blank=True, null=True)
    timestamp = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'watched'
        unique_together = (('userid', 'movieid'),)


class Wish(models.Model):
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    movieid = models.IntegerField(db_column='movieID')  # Field name made lowercase.
    # movieid = models.ForeignKey(Movies)  # Field name made lowercase.
    time = models.DateField(db_column='Time', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wish'
