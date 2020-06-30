from django.test import TestCase

from core.models import *


class TestCourses(TestCase):
    def setUp(self):
        Sex.objects.create(sex='Uomo')
        CustomUser.objects.create(
            username='gaeta92',
            password='acerdata',
            email='panarosagaetano@gmail.com',
            first_name='Gaetano',
            last_name='Panarosa',
            phone='3427749283',
            address='Via Ugo Foscolo 148',
            date_of_birth='1992-04-14',
            town='Mola di Bari',
            codice_fiscale='PNRGTN92D14F280M',
            sex=Sex.objects.get(sex='Uomo')
        )
        Course.objects.create(
            name='Cross Fit',
            description = 'Corso per potersi allenare nelle varie discipline',
            min_subscribers= 10,
            max_subscribers=20,
            price= 45.0,
            start_date= '2020-05-18',
            end_date= '2020-12-31',
            trainer = CustomUser.objects.get(username='gaeta92')
        )
    def testCreateCourse(self):
        self.assertTrue(Course.objects.get(trainer__first_name='Gaetano'))
