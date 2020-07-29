from datetime import datetime

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.views.generic import *

from core.models import CustomUser
from course.models import Course
from prenotation.models.prenotations import Prenotation


class AdminPanelNavbar(TemplateView, PermissionRequiredMixin):
    template_name = 'index_control_panel.html'

    def get(self, request, *args, **kwargs):
        admin = CustomUser.objects.get(pk=request.session['pk'])
        courses_count = Course.objects.filter(active=True).count()
        users_count = CustomUser.objects.filter(groups__name='user').count()
        trainers_count = CustomUser.objects.filter(groups__name='trainer').count()
        prenotations_count = Prenotation.objects.filter(date=datetime.now(), active=True).count()
        courses = Course.objects.filter(active=True)
        return render(request, self.template_name,
                      {'admin': admin, 'courses_count': courses_count, 'users_count': users_count,
                       'trainers_count': trainers_count, 'prenotation_count': prenotations_count, 'courses': courses,
                       'total_accounts': trainers_count + users_count})
