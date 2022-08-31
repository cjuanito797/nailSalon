from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import MinLengthValidator
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManger


# Create your models here.

class User (AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField (_ ('email'), unique=True)
    first_name = models.CharField (max_length=200)
    last_name = models.CharField (max_length=200)
    street_num = models.CharField (max_length=20)
    state = models.CharField (max_length=2)
    zipcode = models.CharField (max_length=5, validators=[MinLengthValidator (5)])
    city = models.CharField (max_length=20)
    phoneNumber = models.CharField (max_length=10, validators=[MinLengthValidator (10)])
    isTechnician = models.BooleanField (default=False)
    is_staff = models.BooleanField (default=False)
    bio = models.TextField (blank=True)

    objects = CustomUserManger ( )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Technician (models.Model):
    user = models.OneToOneField ("Account.User",
                                 related_name='user',
                                 on_delete=models.CASCADE,
                                 default=None)
    bio = models.TextField (blank=True)
    pay_rate = models.DecimalField (decimal_places=2, max_digits=4)
    techSchedule = models.OneToOneField ("Account.Schedule",
                                         related_name='schedule',
                                         on_delete=models.CASCADE,
                                         default=None,
                                         blank=True,
                                         null=True)
    timeSlots = models.OneToOneField("Account.weeklyTimeSlots",
                                     related_name='time slots',
                                     on_delete=models.CASCADE,
                                     default=None,
                                     blank=True,
                                     null=True)


class Schedule (models.Model):
    technician = models.EmailField (_ ('email'), unique=True)

    monday = models.BooleanField (default=False)
    monday_in = models.TimeField ( )
    monday_out = models.TimeField ( )

    tuesday = models.BooleanField (default=False)
    tuesday_in = models.TimeField ( )
    tuesday_out = models.TimeField ( )

    wednesday = models.BooleanField (default=False)
    wednesday_in = models.TimeField ( )
    wednesday_out = models.TimeField ( )

    thursday = models.BooleanField (default=False)
    thursday_in = models.TimeField ( )
    thursday_out = models.TimeField ( )

    friday = models.BooleanField (default=False)
    friday_in = models.TimeField ( )
    friday_out = models.TimeField ( )

    saturday = models.BooleanField (default=False)
    saturday_in = models.TimeField ( )
    saturday_out = models.TimeField ( )

    sunday = models.BooleanField (default=False)
    sunday_in = models.TimeField ( )
    sunday_out = models.TimeField ( )

    def __str__(self):
        return self.technician + '\'s schedule'


class weeklyTimeSlots(models.Model):

    tech = models.EmailField (_ ('email'), unique=True)
    monday_9am = models.BooleanField(default=False)

class Customer (models.Model):
    user = models.OneToOneField ('Account.User',
                                 related_name='customer',
                                 on_delete=models.CASCADE,
                                 default=None)

    # add the appointment history here:

    bio = models.TextField (blank=True)


class Appointment (models.Model):
    phoneNumber = models.CharField (max_length=10, validators=[MinLengthValidator (10)])
