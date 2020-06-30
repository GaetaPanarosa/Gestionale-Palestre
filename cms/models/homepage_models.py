from django.contrib.auth import models


class Carousel(models.Model):
    image = models.ImageField(upload_to='images', null=True, verbose_name='Immagine slider')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.image