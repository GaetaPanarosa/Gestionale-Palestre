from django.views.generic import TemplateView


class UserManagement(TemplateView):
    def get(self, request, *args, **kwargs):
        return (request, self.template_name, {})
