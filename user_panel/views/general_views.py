from django.shortcuts import render
from django.views.generic import *

from core.models import CustomUser, Course


class UserPanelNavbar(TemplateView):
    class Meta:
        abstract = True
    # permission_required = 'index_user'
    def get(self, request, *args, **kwargs):
        user = CustomUser.objects.get(pk = request.session['pk'])
        return render(request, self.template_name, {'user':user})


class UserIndex(UserPanelNavbar):
    def get(self, request, *args, **kwargs):
        courses = Course.objects.all().count()
        return render(request, self.template_name, {'courses':courses})