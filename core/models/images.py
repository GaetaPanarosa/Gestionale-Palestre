from django.db import models


class Images(models.Model):
    image = models.ImageField(upload_to='images', null=True, verbose_name='Immagine')
    active = models.BooleanField(default=True, verbose_name='Attivo')
