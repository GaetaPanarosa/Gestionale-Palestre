from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

from core.forms.users.profile import ProfileForm, AccountForm
from core.models import CustomUser


class UserProfile(TemplateView):
    form_class = ProfileForm()

    def get(self, request, *args, **kwargs):
        form = ProfileForm(instance=get_object_or_404(CustomUser, pk=request.session['pk']))
        account_form = AccountForm(instance=get_object_or_404(CustomUser, pk=request.session['pk']))
        return render(request, self.template_name, {'form': form,'account_form': account_form})
