from django.db import models

from core.models import CustomUser

'''Tipologia Istruttore'''


class TrainerType(models.Model):
    name = models.CharField(max_length=200, verbose_name='Tipo di istruttore', null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


''' Tabella Istruttore '''


class Trainer(models.Model):
    details = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, null=True)
    disponibility = models.BooleanField(default=True, verbose_name='Disponibilità')
    type = models.ForeignKey(TrainerType, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.details.first_name + ' ' + self.details.last_name

    # def __init__(self):
    #     return self.details.get_group_permissions('trainer')
