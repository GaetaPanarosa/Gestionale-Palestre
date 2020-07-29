from django.db import models

''' Tabella Fascia Orarie '''


class Hours(models.Model):
    start_hour = models.TimeField(null=None)
    end_hour = models.TimeField(null=None)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.start_hour.strftime('%H:%M') + ' - ' + self.end_hour.strftime('%H:%M')


class DateRange(models.Model):
    start_date = models.DateField(verbose_name='Inizio fascia', null=True)
    end_date = models.DateField(verbose_name='Fine fascia', null=True)

    def __str__(self):
        return self.start_date.strftime('%d/%m/%Y') + ' - ' + self.end_date.strftime('%d/%m/%Y')
