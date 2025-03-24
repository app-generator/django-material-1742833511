# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Company(models.Model):

    #__Company_FIELDS__
    company_id = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    vat = models.CharField(max_length=255, null=True, blank=True)
    rn = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    web = models.CharField(max_length=255, null=True, blank=True)
    logo = models.CharField(max_length=255, null=True, blank=True)

    #__Company_FIELDS__END

    class Meta:
        verbose_name        = _("Company")
        verbose_name_plural = _("Company")


class Roles(models.Model):

    #__Roles_FIELDS__
    permissions = models.CharField(max_length=255, null=True, blank=True)

    #__Roles_FIELDS__END

    class Meta:
        verbose_name        = _("Roles")
        verbose_name_plural = _("Roles")


class Employee(models.Model):

    #__Employee_FIELDS__
    last_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    hire_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    role_id = models.ForeignKey(roles, on_delete=models.CASCADE)
    status = models.BooleanField()

    #__Employee_FIELDS__END

    class Meta:
        verbose_name        = _("Employee")
        verbose_name_plural = _("Employee")


class Client(models.Model):

    #__Client_FIELDS__
    last_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    date_of_birth = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=255, null=True, blank=True)
    registration_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    status = models.BooleanField()
    subscription_id = models.ForeignKey(subscription, on_delete=models.CASCADE)

    #__Client_FIELDS__END

    class Meta:
        verbose_name        = _("Client")
        verbose_name_plural = _("Client")


class Subscription(models.Model):

    #__Subscription_FIELDS__
    subscription_type = models.CharField(max_length=255, null=True, blank=True)
    price = models.CharField(max_length=255, null=True, blank=True)
    status = models.BooleanField()

    #__Subscription_FIELDS__END

    class Meta:
        verbose_name        = _("Subscription")
        verbose_name_plural = _("Subscription")


class Check_Ins(models.Model):

    #__Check_Ins_FIELDS__
    check_in_id = models.CharField(max_length=255, null=True, blank=True)
    client_id = models.ForeignKey(client, on_delete=models.CASCADE)
    check_in_date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Check_Ins_FIELDS__END

    class Meta:
        verbose_name        = _("Check_Ins")
        verbose_name_plural = _("Check_Ins")


class Transactions(models.Model):

    #__Transactions_FIELDS__
    client_id = models.ForeignKey(client, on_delete=models.CASCADE)
    subscription_id = models.ForeignKey(subscription, on_delete=models.CASCADE)
    price = models.CharField(max_length=255, null=True, blank=True)
    payment_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    payment_method = models.CharField(max_length=255, null=True, blank=True)

    #__Transactions_FIELDS__END

    class Meta:
        verbose_name        = _("Transactions")
        verbose_name_plural = _("Transactions")


class Classes(models.Model):

    #__Classes_FIELDS__
    class_name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    employee_id = models.ForeignKey(employee, on_delete=models.CASCADE)
    start_time = models.DateTimeField(blank=True, null=True, default=timezone.now)
    end_time = models.DateTimeField(blank=True, null=True, default=timezone.now)
    max_participants = models.CharField(max_length=255, null=True, blank=True)
    start_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    end_date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Classes_FIELDS__END

    class Meta:
        verbose_name        = _("Classes")
        verbose_name_plural = _("Classes")


class Bookings(models.Model):

    #__Bookings_FIELDS__
    class_id = models.ForeignKey(classes, on_delete=models.CASCADE)
    client_id = models.ForeignKey(client, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Bookings_FIELDS__END

    class Meta:
        verbose_name        = _("Bookings")
        verbose_name_plural = _("Bookings")


class Schedule(models.Model):

    #__Schedule_FIELDS__
    employee_id = models.ForeignKey(employee, on_delete=models.CASCADE)
    start_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    end_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    start_time = models.DateTimeField(blank=True, null=True, default=timezone.now)
    end_time = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Schedule_FIELDS__END

    class Meta:
        verbose_name        = _("Schedule")
        verbose_name_plural = _("Schedule")



#__MODELS__END
