from django.db import models

from .user_models import CustomUser, Trainer

''' Tabella Fascia Orarie '''
class Hours(models.Model):
    start_hour = models.TimeField(null=None)
    end_hour = models.TimeField(null=None)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.start_hour.strftime('%H:%M') + ' - ' + self.end_hour.strftime('%H:%M')

''' Tabella Corsi '''
class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='Corso', null=True)
    description = models.CharField(max_length=5000, verbose_name='Descrizione', null=True)
    min_subscribers = models.IntegerField(default=0, verbose_name='Numero minimo iscritti')
    max_subscribers = models.IntegerField(default=0, verbose_name='Numero massimo iscritti')
    price = models.DecimalField(max_digits=9, decimal_places=1, default=0, verbose_name='Prezzo', null=True )
    active = models.BooleanField(default=True, verbose_name='Attivo')
    start_date = models.DateField(null=True,verbose_name='Data inizio corso')
    end_date = models.DateField(null=True, verbose_name='Data fine corso')
    trainer = models.ForeignKey(Trainer, on_delete=models.DO_NOTHING, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class CourseDay(models.Model):
    WEEK = (
        (0, 'Lunedi'),
        (1, 'Martedi'),
        (2, 'Mercoledì'),
        (3, 'Giovedì'),
        (4, 'Venerdì'),
        (5, 'Sabato'),
        (6, 'Domenica'),
    )
    day = models.IntegerField(choices=WEEK)
    # hours = models.ManyToManyField(Hours, through_fields='hours', through='CourseDayHoursHours', related_name='hours', related_query_name="hour")
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING, default=None)
    active = models.BooleanField(default=True)


class CourseDayHours(models.Model):
    coursedayhours = models.ForeignKey(CourseDay, on_delete=models.DO_NOTHING, null=True)
    hours = models.ForeignKey(Hours, on_delete=models.DO_NOTHING, null=True)
    active = models.BooleanField(default=True)

class Subscription(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.DO_NOTHING)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    timestamp = models.DateTimeField(auto_now_add=True)

