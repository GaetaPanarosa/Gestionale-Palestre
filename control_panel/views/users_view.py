from django.utils.html import escape
from django.views.generic import TemplateView
from django_datatables_view.base_datatable_view import BaseDatatableView

from core.models import CustomUser


class UserManagement(TemplateView):
    def get(self, request, *args, **kwargs):
        return (request, self.template_name, {})


class UserTable(BaseDatatableView):
    model = CustomUser
    columns = ['first_name', 'last_name', 'phone']
    order_columns = ['first_name', 'last_name', 'phone']

    def get_initial_queryset(self):
        return self.model.objects.filter(groups__name='utente')

    def render_column(self, row, column):
        if column == 'first_name':
            return escape('{0}'.format(row.first_name))
        if column == 'last_name':
            return escape('{0}'.format(row.last_name))
        if column == 'phone':
            return escape('{0}'.format(row.phone))
        else:
            return super(UserTable, self).render_column(row, column)
