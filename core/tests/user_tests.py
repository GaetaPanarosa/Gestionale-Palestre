from django.test import TestCase

from core.models import *


class UserTest(TestCase):
    def setUp(self):
        Sex.objects.create(sex='Uomo')
        CustomUser.objects.create(
            username='gaeta92',
            password='acerdata',
            email='panarosagaetano@gmail.com',
            first_name='Gaetano',
            last_name='Panarosa',
            phone='0804737158',
            address='Via Ugo Foscolo 148',
            date_of_birth='1992-04-14',
            town='Mola di Bari',
            town_birth='Mola di Bari',
            codice_fiscale='PNRGTN92D14F280M',
            sex = Sex.objects.get(sex = 'Uomo')
        )

    def testUser(self):
        self.assertTrue(CustomUser.objects.get(username='gaeta92'))
