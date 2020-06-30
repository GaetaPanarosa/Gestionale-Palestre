from datetime import datetime, timedelta
from pprint import pprint as pp

from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.html import escape
from django.views.generic import TemplateView
from django_datatables_view.base_datatable_view import BaseDatatableView

from core.forms.prenotations.prenotation_form import PrenotationForm
from core.models import Prenotation, Course, CourseDayHours, Hours, CustomUser, CourseDay


class PrenotationManagement(TemplateView):
    form_class = PrenotationForm()
    model = Prenotation

    def get(self, request, *args, **kwargs):
        today = datetime.now()
        latency = 7 - today.isoweekday()
        sunday = today + timedelta(days=latency)
        monday = sunday - timedelta(days=6)
        # count = Prenotation.objects.filter(user_id=int(request.session['pk']),date__gte=monday,  date__lte=sunday).count()
        count = Prenotation.objects.filter(user_id=int(request.session['pk']), date__gte=monday + timedelta(days=7),
                                           date__lte=sunday + timedelta(days=7)).count()
        print('Lunedi: => ', monday, 'Oggi: => ', today, 'Domenica: => ', sunday)
        return render(request, self.template_name, {'form': self.form_class, 'count': count})

    def get_hours(request):
        if request.is_ajax and request.method == 'GET':
            print(request.GET)
            try:
                try:
                    date = datetime.strptime(request.GET.get('date'), '%d/%m/%Y')
                except:
                    date = datetime.strptime(request.GET.get('date'), '%m/%d/%Y')
                # date = datetime.strptime(request.GET.get('date'), '%Y-%m-%d')
                course = Course.objects.get(pk=int(request.GET.get('pk')))
                course_day = CourseDay.objects.filter(day=date.isoweekday() - 1, course=course, course__active=True, active=True).order_by('day').distinct()
                if course_day.count() > 0:
                    hours_course = {}
                    for c in course_day:
                        temp = {}
                        # day = CourseDayHours.objects.filter(coursedayhours__day=int(c.day), coursedayhours_id = int(c.pk), active=True)
                        for d in course_day:
                            temp['name'] = d.course.name
                            temp['day'] = d.get_day_display()
                            temp['hours'] = []
                            for h in CourseDayHours.objects.filter(coursedayhours_id=d.pk, coursedayhours__course = d.course,  active=True).order_by(
                                    'hours__start_hour'):
                                temp['hours'].append({'id': h.hours.pk, 'start_hour': h.hours.start_hour.strftime('%H:%M'),
                                                      'end_hour': h.hours.end_hour.strftime('%H:%M')})
                    hours_course = (temp['hours'])
                    pp(hours_course)
                    response = {'status': '200', 'reason': 'Fasce orarie trovate', 'hours': hours_course,
                                'course_name': course.name}
                    return JsonResponse(response, safe=False, content_type='application/json')
                if course_day == course.max_subscribers:
                    response = {'status': '500',
                                'reason': 'Non ci sono più posti disponibili per questo giorno.'}
                    return JsonResponse(response, safe=False, content_type='application/json')
                response = {'status': '500', 'reason': 'Questo corso non ha fasce orarie disponibili per questo giorno'}
                return JsonResponse(response, safe=False, content_type='application/json')
            except Exception as e:
                print(e)
                response = {'status': '500', 'reason': 'Impossibile trovare fasce orarie'}
                return JsonResponse(response, safe=False, content_type='application/json')
            return JsonResponse(response, safe=False, content_type='application/json')

    def check_disponibility(request):
        print(request.GET)
        try:
            date = datetime.strptime(request.GET.get('date'), '%d/%m/%Y')
        except:
            date = datetime.strptime(request.GET.get('date'), '%m/%d/%Y')
        if request.is_ajax and request.method == 'GET':
            query = Prenotation.objects.filter(course=request.GET.get('course'), date=date,
                                               time=Hours.objects.get(pk=int(request.GET.get('pk_hour'))), active = True)
            if not query.exists():
                response = {'status': '200', 'reason': 'Posti disponibili',
                            'counts': Course.objects.get(pk=request.GET.get('course')).max_subscribers}
                return JsonResponse(response, safe=False, content_type='application/json')

            if query.count() < query.first().course.max_subscribers:
                response = {'status': '200', 'reason': 'Posti disponibili',
                            'counts': query.first().course.max_subscribers - query.count()}
                return JsonResponse(response, safe=False, content_type='application/json')
            if query.count() == query.first().course.max_subscribers:
                response = {'status': '500', 'reason': 'Non ci sono più posti disponibili per questa fascia oraria.'}
                return JsonResponse(response, safe=False, content_type='application/json')

        raise PermissionDenied

    def prenotation(request):
        if request.is_ajax and request.method == 'POST':
            print(request.POST)
            try:

                find_prenotation = Prenotation.objects.filter(user_id=int(request.session['pk']),
                                                              course_id=int(request.POST.get('course')),
                                                              day=datetime.strptime(request.POST.get('date_form'),
                                                                                    '%d/%m/%Y').isoweekday() - 1,
                                                              time_id=int(request.POST.get('course_hours')),
                                                              date=datetime.strptime(request.POST.get('date_form'),
                                                                                     '%d/%m/%Y'),active=True)
                if find_prenotation.count() > 0:
                    response = {'status': '500', 'reason': 'Ti sei già prenotato in questo giorno!'}
                    return JsonResponse(response, safe=False, content_type='application/json')

                today = datetime.now() + timedelta(minutes=30)
                print(today)
                date = datetime.strptime(request.POST.get('date_form'),'%d/%m/%Y') + timedelta(
                    hours=Hours.objects.get(pk = int(request.POST.get('course_hours'))).start_hour.hour,
                                            minutes=Hours.objects.get(pk= int(request.POST.get('course_hours'))).end_hour.minute)
                print(date)
                if today > date:
                    response = {'status': '500',
                                'reason': 'La prenotazione può essere effettuata massimo 1h prima dall\'inizio del corso'}
                    return JsonResponse(response, safe=False, content_type='application/json')

                prenotation = Prenotation()
                prenotation.user = CustomUser.objects.get(pk=request.session['pk'])
                prenotation.course = Course.objects.get(pk=int(request.POST.get('course')))
                prenotation.date = datetime.strptime(request.POST.get('date_form'), '%d/%m/%Y')
                prenotation.day = datetime.strptime(request.POST.get('date_form'), '%d/%m/%Y').isoweekday() - 1
                prenotation.time = Hours.objects.get(pk=int(request.POST.get('course_hours')))
                prenotation.save()
                response = {'status': '200', 'reason': 'Prenotazione effettuata con successo!'}
                return JsonResponse(response, safe=False, content_type='application/json')
            except Exception as e:
                print(e)
                response = {'status': '500', 'reason': 'Impossibile effettuare la prenotazione'}
                return JsonResponse(response, safe=False, content_type='application/json')
            return JsonResponse(response, safe=False, content_type='application/json')
        raise PermissionDenied

    def dismiss_prenotation(request):
        print(request.GET)
        if request.is_ajax and request.method == 'GET':
            date = datetime.strptime(request.GET.get('date'), '%Y-%m-%d')
            print(date)
            prenotation = Prenotation.objects.get(pk=int(request.GET.get('pk')), date=date)


            today = datetime.now() + timedelta(minutes=30)
            print(today)
            date = date + timedelta(hours=prenotation.time.start_hour.hour, minutes=prenotation.time.end_hour.minute)
            print(date)
            if today > date:
                response = {'status': '500', 'reason': 'La disdetta può essere effettuata massimo 30 minuti prima dall\'inizio del corso'}
                return JsonResponse(response, safe=False, content_type='application/json')
            prenotation.active=False
            prenotation.save()
            response = {'status': '200','reason':'La prenotazione è stata cancellata con successo'}
            return JsonResponse(response, safe=False, content_type='application/json')

        raise PermissionDenied


class PrenotationUserTable(BaseDatatableView):
    model = Prenotation
    columns = ['course', 'date', 'dismiss']
    order_columns = ['course', 'date', '']

    def get_initial_queryset(self):
        return self.model.objects.filter(user=int(self.request.session['pk']), active=True).order_by('-date')

    def render_column(self, row, column):
        if column == 'date':
            return escape('{0} {1} {2} - {3}'.format(row.get_day_display(), row.date.strftime('%d/%m/%Y'),
                                                     row.time.start_hour.strftime('%H:%M'),
                                                     row.time.end_hour.strftime('%H:%M')))
        if column == 'course':
            return escape('{0}'.format(row.course.name))
        if column == 'dismiss':
            date = '\'' + datetime.strftime(row.date, '%Y-%m-%d') + '\''
            return '<a href="#" onclick="dismissPrenotation(' + str(row.pk) + ',' + str(
                date) + ')"><button class="btn btn-danger" type="button">Disdici</button></a>'
        else:
            return super(PrenotationUserTable, self).render_column(row, column)

    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(
                Q(course__name__icontains=search) | Q(date__icontains=search) | Q(
                    time__start_hour__icontains=search) | Q(time__end_hour__icontains=search))
        return qs
