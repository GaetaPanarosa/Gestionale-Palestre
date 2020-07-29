from datetime import datetime, timedelta

from django.core.exceptions import PermissionDenied
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from course.models import CourseDay, Course, CourseDayHours
from prenotation.models.prenotations import Prenotation


class PrenotationManagementAdmin(TemplateView):
    def get(self, request, *args, **kwargs):
        form_class = PrenotationForm()
        template_name = 'control_panel/prenotation/prenotation.html'
        return render(request, template_name, {'form': form_class})

    def get_hours(request):
        if request.is_ajax and request.method == 'GET':
            print(request.GET.get('date').split('T'))
            try:
                # try:
                #     date = datetime.strptime(json.dumps(request.GET.get('date')), '%d/%m/%Y')
                # except:
                #     date = datetime.strptime(json.dumps(request.GET.get('date')), '%m/%d/%Y')
                date = datetime.strptime(request.GET.get('date').split('T')[0], '%Y-%m-%d') + timedelta(days=1)
                print(date.isoweekday())
                course_day = CourseDay.objects.filter(day=int(date.isoweekday() - 1),
                                                      course=Course.objects.get(pk=int(request.GET.get('pk_course'))),
                                                      active=True)
                if course_day.count() > 0:
                    hours_course = {}
                    for p in course_day:
                        temp = {}
                        day = CourseDayHours.objects.filter(coursedayhours=p.pk, active=True).order_by(
                            'hours__start_hour')
                        for d in day:
                            temp['hours'] = []
                            for h in CourseDayHours.objects.filter(coursedayhours_id=d.coursedayhours.pk, active=True,
                                                                   hours__active=True,
                                                                   coursedayhours__active=True).order_by(
                                    'hours__start_hour'):
                                temp['hours'].append(
                                    {'id': h.hours.pk, 'start_hour': h.hours.start_hour.strftime('%H:%M'),
                                     'end_hour': h.hours.end_hour.strftime('%H:%M')})
                        hours_course = temp['hours']
                    # pp(hours_course)
                    response = {'status': '200', 'reason': 'Fasce orarie trovate', 'hours': hours_course}
                    return JsonResponse(response, safe=False, content_type='application/json')
                # if course_day_hours == course.max_subscribers:
                #     response = {'status': '500',
                #                 'reason': 'Non ci sono più posti disponibili per questo giorno.'}
                #     return JsonResponse(response, safe=False, content_type='application/json')
                response = {'status': '500', 'reason': 'Questo corso non ha fasce orarie disponibili per questo giorno'}
                return JsonResponse(response, safe=False, content_type='application/json')
            except Exception as e:
                print(e)
                response = {'status': '500', 'reason': 'Impossibile trovare fasce orarie'}
                return JsonResponse(response, safe=False, content_type='application/json')
            return JsonResponse(response, safe=False, content_type='application/json')

    def check_disponibility(request):
        print(request.GET.get('date').split('T'))
        # try:
        #     date = datetime.strptime(request.GET.get('date'), '%d/%m/%Y')
        # except:
        #     date = datetime.strptime(request.GET.get('date'), '%m/%d/%Y')
        if request.is_ajax and request.method == 'GET':
            date = datetime.strptime(request.GET.get('date').split('T')[0], '%Y-%m-%d')

            query = Prenotation.objects.filter(course=request.GET.get('course'), date=date,
                                               time=Hours.objects.get(pk=int(request.GET.get('pk_hour'))))
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


class PrenotationDetails(TemplateView):
    def get(self, request, *args, **kwargs):
        prenotation = Prenotation.objects.get(pk=int(self.kwargs['pk']))
        form_class = ModPrenotationForm(instance=prenotation)
        disable_days = []
        for p in Prenotation.objects.filter(active=True):
            if p.count >= 15:
                disable_days.append(p.date)
        return render(request, self.template_name,
                      {'prenotation': prenotation, 'form': form_class, 'days': disable_days})

    def post(self, request, *args, **kwargs):
        print(request.POST, self.kwargs['pk'])
        prenotation = Prenotation.objects.get(pk=int(self.kwargs['pk']))
        print(prenotation)
        form_class = ModPrenotationForm(instance=prenotation)
        if form_class.is_valid():
            print('ok')
            return JsonResponse({'status': '200', 'reason': 'ok '})
        return JsonResponse({'status': '500', 'reason': 'Errore'})
