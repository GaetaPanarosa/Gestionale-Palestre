from core.models import Hours, DateRange, Images
from trainer.models import *

''' Tabella Corsi '''


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='Corso', null=True)
    description = models.CharField(max_length=5000, verbose_name='Descrizione', null=True)
    min_subscribers = models.IntegerField(default=0, verbose_name='Numero minimo iscritti')
    max_subscribers = models.IntegerField(default=0, verbose_name='Numero massimo iscritti')
    price = models.DecimalField(max_digits=9, decimal_places=1, default=0, verbose_name='Prezzo', null=True)
    active = models.BooleanField(default=True, verbose_name='Attivo')
    start_date = models.DateField(null=True, verbose_name='Data inizio corso')
    end_date = models.DateField(null=True, verbose_name='Data fine corso')
    trainer = models.ForeignKey(Trainer, on_delete=models.DO_NOTHING, null=True)

    # n_max_prenotation = models.IntegerField(verbose_name='Numero di posti')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


''' Tabella associazione corso - giorno della settimana '''


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


''' Tabella associazione corso -  giorno della settimana - fasce orarie '''


class CourseDayHours(models.Model):
    coursedayhours = models.ForeignKey(CourseDay, on_delete=models.DO_NOTHING, null=True)
    hours = models.ForeignKey(Hours, on_delete=models.DO_NOTHING, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.coursedayhours.course.name + ' - ' + self.hours.start_hour.strftime(
            '%H:%M') + ' - ' + self.hours.end_hour.strftime('%H:%M')


''' Tabella impostazioni corso'''


class CourseSettings(models.Model):
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING, null=True)
    time_dismiss_hour = models.IntegerField(verbose_name='Tempo di disdetta in ore')
    time_dismiss_minutes = models.IntegerField(verbose_name='Tempo di disdetta in minuti')
    time_dismiss_secondi = models.IntegerField(verbose_name='Tempo di disdetta in secondi')
    time_prenotation_hour = models.IntegerField(verbose_name='Tempo di prenotazione in ore')
    time_prenotation_minutes = models.IntegerField(verbose_name='Tempo di prenotazione in minuti')
    time_prenotation_secondi = models.IntegerField(verbose_name='Tempo di prenotazione in secondi')

    def __str__(self):
        return self.course.name


''' Tabella disattivazione corso per un determinato periodo di tempo o solo per un giorno '''


class DisactiveCourseOnDay(models.Model):
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING, null=True)
    date = models.DateField(verbose_name='Giorno da disattivare', null=True)
    active = models.BooleanField(default=False)
    dateRange = models.ForeignKey(DateRange, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        if self.dateRange:
            return self.course.name + ' - ' + self.date.strftime('%d/%m/%Y')
        else:
            return self.course.name + ' - ' + self.dateRange.start_date.strftime(
                '%d/%m/%Y') + ' - ' + self.dateRange.end_date.strftime('%d/%m/%Y')


class CourseImages(models.Model):
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING, null=True)
    image = models.ForeignKey(Images, on_delete=models.DO_NOTHING, null=True)
    thumbnail = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.image.image.name


'''Tabella Personal Trainer'''


class PersonalTrainer(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, null=True)
    trainer = models.ForeignKey(Trainer, on_delete=models.DO_NOTHING, null=True)
    active = models.BooleanField(default=True)


class PersonalTrainerCourse(models.Model):
    personalTrainer = models.ForeignKey(PersonalTrainer, on_delete=models.DO_NOTHING, null=True)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING, null=True)
    price = models.FloatField(default=0.0, verbose_name='Prezzo dell\'istruttore')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.personalTrainer.trainer.details.first_name + ' ' + self.personalTrainer.trainer.details.last_name + ' - ' + self.personalTrainer.user.first_name + ' ' + self.personalTrainer.user.last_name + ' - ' + str(
            self.price) + ' - ' + self.course.name
