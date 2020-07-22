from django.utils.html import escape
from django_datatables_view.base_datatable_view import BaseDatatableView

from course.models import Course


class CourseTable(BaseDatatableView):
    model = Course
    columns = ['name', 'start_date', 'end_date', 'price', 'trainer', 'details', 'disable']
    order_columns = ['name', 'start_date', 'end_date', 'price', 'trainer', '', '']

    def get_initial_queryset(self):
        return self.model.objects.filter(active=True).order_by('-name')

    def render_column(self, row, column):
        if column == 'name':
            return escape('{0}'.format(row.name))
        if column == 'start_date':
            return escape('{0}'.format(row.start_date.strftime('%d/%m/%Y')))
        if column == 'end_date':
            return escape('{0}'.format(row.end_date.strftime('%d/%m/%Y')))
        if column == 'price':
            if row.price:
                return escape('{0}'.format(row.price))
            else:
                return 'Nessun prezzo'
        if column == 'trainer':
            if row.trainer is not None:
                return escape('{0} {1}'.format(row.trainer.details.first_name, row.trainer.details.last_name))
            else:
                return 'Nessun istruttore'
        if column == 'details':
            return '<a href="dettaglio_corso/%s/">Vedi dettaglio <i class="iconsminds-arrow-forward-2"></i></a>' % row.pk
        if column == 'disable':
            return '<a href="#" onclick="disableCourse(' + str(
                row.pk) + ')"><button class="btn btn-danger" type="button">Disattiva</button></a>'
        else:
            return super(CourseTable, self).render_column(row, column)


class CourseDisactivatedTable(BaseDatatableView):
    model = Course
    columns = ['name', 'start_date', 'end_date', 'price', 'trainer', 'details', 'enable']
    order_columns = ['name', 'start_date', 'end_date', 'price', 'trainer', '', '']

    def get_initial_queryset(self):
        return self.model.objects.filter(active=False).order_by('-name')

    def render_column(self, row, column):
        if column == 'name':
            return escape('{0}'.format(row.name))
        if column == 'start_date':
            return escape('{0}'.format(row.start_date.strftime('%d/%m/%Y')))
        if column == 'end_date':
            return escape('{0}'.format(row.end_date.strftime('%d/%m/%Y')))
        if column == 'price':
            if row.price:
                return escape('{0}'.format(row.price))
            else:
                return 'Nessun prezzo'
        if column == 'trainer':
            if row.trainer:
                return escape('{0} {1}'.format(row.trainer.details.first_name, row.trainer.details.last_name))
            else:
                return 'Nessun istruttore'
        if column == 'details':
            return '<a href="dettaglio_corso/%s/">Vedi dettaglio <i class="iconsminds-arrow-forward-2"></i></a>' % row.pk
        if column == 'enable':
            return '<a href="#" onclick="enableCourse(' + str(
                row.pk) + ')"><button class="btn btn-success" type="button">Riattiva</button></a>'
        else:
            return super(CourseDisactivatedTable, self).render_column(row, column)
