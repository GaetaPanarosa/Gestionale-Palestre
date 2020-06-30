from django.db import models

from core.models import Course


class CourseImages(models.Model):
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING, null=True)
    image = models.ImageField(upload_to='images',null=True)
    thumbnail = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

