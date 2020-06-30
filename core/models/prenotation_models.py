from django.db import models

from .courses_models import Course, Hours
from .user_models import CustomUser

#
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

class PrenotationSettings(models.Model):
    dismiss_prenotation = models.IntegerField(default=2)
    active = models.BooleanField(default=True)
