from datetime import datetime

from django.shortcuts import render
from django.views.generic import *

from core.models import CustomUser, Course, Prenotation


class AdminPanelNavbar(TemplateView):
    # permission_required = 'index_user'
    def get(self, request, *args, **kwargs):
        admin = CustomUser.objects.get(pk = request.session['pk'])
        courses = Course.objects.all().count()
        users = CustomUser.objects.filter(groups__name='utente').count()
        prenotations = Prenotation.objects.filter(date= datetime.now(), active=True).count()
        return render(request, self.template_name, {'admin':admin,'courses':courses,'users':users, 'prenotations': prenotations})
