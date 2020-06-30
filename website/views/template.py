from django.shortcuts import render

from core.auth.views import LoginView


class NavbarTemplate(LoginView):
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form_login': LoginView.form_class})