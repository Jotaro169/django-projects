# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    admin_name = models.CharField(max_length=45)
    admin_image = models.CharField(max_length=200)
    admin_email = models.CharField(max_length=50)
    password = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'admin'


class Area(models.Model):
    pincode = models.IntegerField(primary_key=True)
    area_name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'area'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
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
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    car = models.ForeignKey('Car', models.DO_NOTHING)
    cust = models.ForeignKey('Customer', models.DO_NOTHING)
    amt = models.FloatField()
    pick_add = models.CharField(max_length=200)
    drop_add = models.CharField(max_length=200)
    status = models.CharField(max_length=10)
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()
    pick_pincode = models.ForeignKey(Area, models.DO_NOTHING, db_column='pick_pincode')
    drop_pincode = models.ForeignKey(Area, models.DO_NOTHING, db_column='drop_pincode', related_name='booking_drop_pincode_set')

    class Meta:
        managed = False
        db_table = 'booking'


class Car(models.Model):
    car_id = models.AutoField(primary_key=True)
    company_id = models.IntegerField()
    registration_no = models.CharField(max_length=10)
    car_image = models.ImageField(upload_to='img/')
    model_year = models.IntegerField()
    is_manual = models.IntegerField()
    mileage = models.IntegerField()
    fuel_type = models.IntegerField()
    car_type = models.CharField(max_length=20)
    model_name = models.CharField(max_length=45)
    capacity = models.IntegerField()
    color = models.CharField(max_length=10)
    charge = models.FloatField()
    # razor_pay_order_id = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'car'


class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'company'


class Customer(models.Model):
    cust_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    phone_no = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    dl_no = models.CharField(max_length=16)
    address = models.CharField(max_length=200)
    password = models.CharField(max_length=16)
    dl_image = models.CharField(max_length=200)
    is_verified = models.IntegerField()
    cust_image = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'customer'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
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
    id = models.BigAutoField(primary_key=True)
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


class Feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    cust = models.ForeignKey(Customer, models.DO_NOTHING)
    car = models.ForeignKey(Car, models.DO_NOTHING)
    description = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'feedback'


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    booking = models.ForeignKey(Booking, models.DO_NOTHING)
    cust = models.ForeignKey(Customer, models.DO_NOTHING)
    transaction = models.IntegerField()
    status = models.IntegerField()
    payment_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'payment'
