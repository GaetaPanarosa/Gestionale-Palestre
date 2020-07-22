from django.contrib.auth.models import AbstractUser
from django.db import models

''' Tabella sesso '''


class Sex(models.Model):
    sex = models.CharField(max_length=50)

    def __str__(self):
        return self.sex


''' Tabella Utenti '''


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=10, null=True, verbose_name='Telefono', default=None)
    date_of_birth = models.DateField(null=True, verbose_name='Data di Nascita', default=None)
    codice_fiscale = models.CharField(max_length=16, verbose_name='Codice Fiscale')
    address = models.CharField(max_length=200, verbose_name='Indirizzo', default=None, null=True)
    town = models.CharField(max_length=200, verbose_name='Città/Paese', null=True)
    sex = models.ForeignKey(Sex, on_delete=models.DO_NOTHING, verbose_name='Sesso', null=True)
    town_birth = models.CharField(max_length=200, verbose_name='Città di nascita', null=True)
    image = models.ImageField(upload_to='media', verbose_name='Immagine del profilo', null=True,
                              default='user_default.jpg')

    def __str__(self):
        return str(self.first_name) + ' ' + str(self.last_name)
