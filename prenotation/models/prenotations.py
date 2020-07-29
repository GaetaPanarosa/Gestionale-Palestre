from django.db import models

from core.models import CustomUser, Hours
from course.models import Course

''' Tabella Prenotazioni '''


class Prenotation(models.Model):
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
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, null=True)
    time = models.ForeignKey(Hours, on_delete=models.DO_NOTHING, null=True)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING, null=True)
    timestamp = models.DateTimeField(auto_now_add=True),
    date = models.DateField()
    active = models.BooleanField(default=True)

    def __str__(self):
        prenotation = self.user.first_name + ' - ' + self.user.last_name + ' - ' + ' - ' + self.course.name + ' - ' + self.date.strftime()
        return


class PrenotationSettings(models.Model):
    dismiss_prenotation = models.IntegerField(default=2)
    active = models.BooleanField(default=True)
