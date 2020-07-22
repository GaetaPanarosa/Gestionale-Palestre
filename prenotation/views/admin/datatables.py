from datetime import datetime

from django.db.models import Q
from django.utils.html import escape
from django_datatables_view.base_datatable_view import BaseDatatableView

from core.models import Hours
from course.models import Course
from prenotation.models.prenotations import Prenotation


class PrenotationTable(BaseDatatableView):
    model = Prenotation
    columns = ['date', 'details']
    order_columns = ['date', '']

    def get_initial_queryset(self):

        return self.model.objects.all().order_by('-date').distinct('date')

    def render_column(self, row, column):
        if column == 'date':
            return escape('{0}'.format(row.date.strftime('%d/%m/%Y')))
        if column == 'details':
            return '<a href="/control_panel/prenotazioni/dettaglio_prenotazione/%s/">Vedi prenotazioni <i class="fa fa-arrow-right"></i></a>' % str(
                row.date)
        else:
            return super(PrenotationTable, self).render_column(row, column)


class PrenotationDetailsTable(BaseDatatableView):
    model = Prenotation
    columns = ['user', 'phone', 'modify', 'disable']
    order_columns = ['user', 'phone', '', '']

    def get_initial_queryset(self):
        print(self.kwargs['date'].split('T')[0])
        date = datetime.strptime(self.kwargs['date'].split('T')[0], '%Y-%m-%d')
        if Course.objects.all().count() > 0:
            return self.model.objects.filter(active=True, course=Course.objects.get(pk=int(self.kwargs['course'])),
                                             date=date, day=int(date.isoweekday() - 1),
                                             time=Hours.objects.get(pk=int(self.kwargs['pk'])))
        return self.model.objects.all()

    def render_column(self, row, column):
        if column == 'user':
            return escape('{0} {1}'.format(row.user.first_name, row.user.last_name))
        if column == 'phone':
            return escape('{0}'.format(row.user.phone))
        if column == 'modify':
            return '<a href="/control_panel/prenotazioni/dettaglio_prenotazione/%s/"><button class="btn btn-primary btn-sm" type="button">Modifica questa prentoazione</button></a>' % row.pk
        if column == 'disable':
            return '<a href="#" onclick="dismissPrenotation(' + str(
                row.pk) + ')"><button class="btn btn-danger btn-sm" type="button">Disdici questa prenotazione</button></a>'
        else:
            return super(PrenotationDetailsTable, self).render_column(row, column)

    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(
                Q(first_name__icontains=search) | Q(last_name__icontains=search) | Q(phone__icontains=search))
        return qs
