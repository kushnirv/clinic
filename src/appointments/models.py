from django.utils import timezone
from django.db import models
from django.db.models import Q
from datetime import timedelta, time
from django.core.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist

# Create your models here.


class Specialization(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    full_name = models.CharField(max_length=100)
    specialization = models.ForeignKey(Specialization)

    def __str__(self):
        return self.full_name


class Appointment(models.Model):
    full_name = models.CharField(max_length=100)
    date = models.DateTimeField()
    doctor = models.ForeignKey(Doctor)

    def __str__(self):
        return self.full_name

    def clean(self):
        try:
            doctor = self.doctor
        except ObjectDoesNotExist:
            return
        if self.date is None:
            return

        count = Appointment.objects\
            .filter(doctor=doctor)\
            .filter(
                Q(
                    date__gte=self.date,
                    date__lte=self.date + timedelta(hours=1)
                ) |
                Q(
                    date__gt=self.date - timedelta(hours=1),
                    date__lt=self.date
                )
            ).count()

        if count > 0:
            raise ValidationError({'date': 'Выбранное время занято.'})

        if (self.date.time() < time(9, 0)) or (self.date.time() > time(17, 0)):
            raise ValidationError(
                {'date': 'Время работы поликлиники 9:00 - 18:00'}
            )

        if self.date.weekday() >= 5:
            raise ValidationError(
                {'date': 'Выходные дни Суббота, Воскресенье'}
            )

        if self.date < timezone.now():
            raise ValidationError(
                {'date': 'Запись на этот день окончена'}
            )
