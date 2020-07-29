import json
import logging

from django.core.exceptions import PermissionDenied
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import *

from core.forms import *
from course.forms import *
from course.models import *
from trainer.forms import *


class CourseManagement(FormView):
    form_class = CourseForm
    form_trainer = TrainerForm
    form_trainer_user = TrainerFormRegister
    form_hours = HoursForm
    form_m2m = CourseDayForm

    def get(self, request, *args, **kwargs):
        count_hours = Hours.objects.all().count()
        count_trainers = Trainer.objects.filter(details__groups__name='istruttore').count()
        return render(request, self.template_name, {
            'form': self.form_class,
            'form_trainer': self.form_trainer,
            'form_trainer_user': self.form_trainer_user,
            'form_m2m': self.form_m2m,
            'form_hours': self.form_hours,
            'count_hours': count_hours,
            'count_trainers': count_trainers,
        })

    def post(self, request, *args, **kwargs):
        if request.is_ajax and request.method == 'POST':
            form_corso = CourseForm(request.POST)
            if form_corso.is_valid():
                form_corso.save()
                response = {'status': '200', 'reason': 'Corso inserito con successo.'}
                return JsonResponse(response, safe=False, content_type="application/json")
            logging.basicConfig(filename='example.log', level=logging.DEBUG)
            logging.debug(form_corso.errors)
            response = {'status': '500', 'reason': [v[0] for k, v in form_corso.errors.items()]}
            return JsonResponse(response, safe=False, content_type="application/json")

    def details_course(request, pk):
        template_name = 'detail_course.html'
        course = Course.objects.get(pk=pk)
        course_day_hours = CourseDay.objects.filter(course=course, course__active=True).order_by('day').distinct()
        hours_course = []
        hours_course_disactivated = []
        form_hours = HoursForm
        form_m2m = CourseDayForm
        form_course = ModifyCourseForm(instance=course)
        for c in course_day_hours:
            temp = {}
            day = CourseDay.objects.filter(day=int(c.day), course=course, course__active=True, active=True)
            for d in day:
                temp['pk'] = d.pk
                temp['name'] = d.course.name
                temp['day_name'] = d.get_day_display()
                temp['day'] = d.day
                temp['hours'] = []
                for h in CourseDayHours.objects.filter(coursedayhours_id=d.pk, active=True).order_by(
                        'hours__start_hour'):
                    temp['hours'].append(model_to_dict(h.hours))
                hours_course.append(temp)
        for c in course_day_hours:
            temp = {}
            day = CourseDay.objects.filter(day=int(c.day), course=course, course__active=True)
            for d in day:
                temp['pk'] = d.pk
                temp['name'] = d.course.name
                temp['day_name'] = d.get_day_display()
                temp['day'] = d.day
                temp['hours'] = []
                for h in CourseDayHours.objects.filter(coursedayhours_id=d.pk, active=False).order_by(
                        'hours__start_hour'):
                    temp['hours'].append(model_to_dict(h.hours))
                hours_course_disactivated.append(temp)
        active_days = CourseDay.objects.filter(course=course, active=True)
        disactivated_days = CourseDay.objects.filter(course=course, active=False)
        print(active_days, disactivated_days)
        return render(request, template_name,
                      {'course': course, 'hours': hours_course, 'course_day_hours': course_day_hours,
                       'form': form_course, 'form_m2m': form_m2m, 'hours_restore': hours_course_disactivated,
                       'form_hours': form_hours, 'pk': pk, 'active_days': active_days,
                       'disactivated_days': disactivated_days})

    def disactiveCourse(request):
        print(request)
        if request.is_ajax and request.method == 'GET':
            try:
                Course.objects.filter(pk=int(request.GET.get('pk'))).update(active=False)
                response = {'status': '200', 'reason': 'Corso disattivato correttamente.'}
                return JsonResponse(response, safe=False, content_type="application/json")
            except Exception as e:
                print(e)
                response = {'status': '500', 'reason': 'Si è verificato un errore.'}
                return JsonResponse(response, safe=False, content_type="application/json")
        raise PermissionDenied

    def enableCourse(request):
        print(request)
        if request.is_ajax and request.method == 'GET':
            try:
                Course.objects.filter(pk=int(request.GET.get('pk'))).update(active=True)
                response = {'status': '200', 'reason': 'Corso riattivato correttamente.'}
                return JsonResponse(response, safe=False, content_type="application/json")
            except Exception as e:
                print(e)
                response = {'status': '500', 'reason': 'Si è verificato un errore.'}
                return JsonResponse(response, safe=False, content_type="application/json")
        raise PermissionDenied

    def disableDay(request):
        print(request)
        if request.is_ajax and request.method == 'GET':
            try:
                CourseDay.objects.filter(pk=int(request.GET.get('pk'))).update(active=False)
                response = {'status': '200', 'reason': 'Giorno disattivato correttamente.'}
                return JsonResponse(response, safe=False, content_type="application/json")
            except Exception as e:
                print(e)
                response = {'status': '500', 'reason': 'Si è verificato un errore.'}
                return JsonResponse(response, safe=False, content_type="application/json")
        raise PermissionDenied

    # def deleteDay(request):
    #     print(request)
    #     if request.is_ajax and request.method == 'DELETE':
    #         try:
    #             CourseDay.objects.filter(pk=int(request.DELETE.get('pk_course')), day=int(request.DELETE.get('day'))).delete()
    #             response = {'status': '200', 'reason': 'Giorno cancellato correttamente.'}
    #             return JsonResponse(response, safe=False, content_type="application/json")
    #         except Exception as e:
    #             print(e)
    #             response = {'status': '500', 'reason': 'Si è verificato un errore.'}
    #             return JsonResponse(response, safe=False, content_type="application/json")
    #     raise PermissionDenied

    def restoreDay(request):
        print(request)
        if request.is_ajax and request.method == 'GET':
            try:
                CourseDay.objects.filter(pk=int(request.GET.get('pk'))).update(active=True)
                response = {'status': '200', 'reason': 'Giorno riattivato correttamente.'}
                return JsonResponse(response, safe=False, content_type="application/json")
            except Exception as e:
                print(e)
                response = {'status': '500', 'reason': 'Si è verificato un errore.'}
                return JsonResponse(response, safe=False, content_type="application/json")
        raise PermissionDenied


class CourseDayHoursView(FormView):
    def post(self, request, *args, **kwargs):
        if request.is_ajax and request.method == 'POST':
            form_corso = CourseDayForm(request.POST)
            if form_corso.is_valid():
                corso_query = CourseDay.objects.filter(course=form_corso.cleaned_data['course'],
                                                       day=form_corso.cleaned_data['day'])
                if not corso_query.exists():
                    corso = form_corso.save(commit=False)
                    corso.save()
                    for hour in json.loads(request.POST.get('hours_arr')):
                        add_hours_to_course = CourseDayHours()
                        add_hours_to_course.coursedayhours_id = corso_query.first().pk
                        add_hours_to_course.hours = Hours.objects.get(pk=int(hour))
                        add_hours_to_course.save()
                    response = {'status': '200', 'reason': 'Giorni e fasce inserite con successo.'}
                    return JsonResponse(response, safe=False, content_type="application/json")
                else:
                    corso_query = CourseDay.objects.filter(course=form_corso.cleaned_data['course'],
                                                           day=form_corso.cleaned_data['day']).first()
                    for hour in json.loads(request.POST.get('hours_arr')):
                        add_hours_to_course = CourseDayHours()
                        add_hours_to_course.coursedayhours_id = corso_query.pk
                        add_hours_to_course.hours = Hours.objects.get(pk=int(hour))
                        add_hours_to_course.save()
                    response = {'status': '200', 'reason': 'Corso aggiornato.'}
                    return JsonResponse(response, safe=False, content_type="application/json")
            response = {'status': '500', 'reason': 'Si è verificato un errore.'}
            return JsonResponse(response, safe=False, content_type="application/json")

    def disableHourFromCourse(request):
        if request.is_ajax and request.method == 'GET':
            print('Riattiva fascia request: ', request.GET)
            course = Course.objects.get(pk=int(request.GET.get('pk_course')))
            hours = Hours.objects.get(pk=int(request.GET.get('hour_list')))
            course_day_hours = CourseDay.objects.get(course=course, day=int(request.GET.get('day_hour')))
            try:
                hour_to_disable = CourseDayHours.objects.filter(coursedayhours__course=course,
                                                                coursedayhours__day=int(request.GET.get('day_hour')),
                                                                hours=hours).first()
                print(hour_to_disable)
                hour_to_disable.active = False
                hour_to_disable.save()
                response = {'status': '200', 'reason': 'Hai disabilitato la fascia ' + str(
                    hours.start_hour.strftime('%H:%M')) + ' - ' + str(
                    hours.end_hour.strftime('%H:%M')) + ' per il giorno ' + str(
                    course_day_hours.get_day_display()) + ''}
                return JsonResponse(response, safe=False, content_type='application/json')
            except Exception as e:
                print(e)
                response = {'status': '500', 'reason': 'Si è verificato un errore.'}
                return JsonResponse(response, safe=False, content_type='application/json')
        raise PermissionDenied

    def restore_hours_for_day(request):
        if request.is_ajax and request.method == 'GET':
            print('Riattiva fascia request: ', request.GET)
            course = Course.objects.get(pk=int(request.GET.get('pk_course_restore')))
            hours = Hours.objects.get(pk=int(request.GET.get('hour_list_restore')))
            course_day_hours = CourseDay.objects.get(course=course, day=int(request.GET.get('day_hour_restore')))
            try:
                hour_to_disable = CourseDayHours.objects.get(coursedayhours__course=course,
                                                             coursedayhours__day=int(
                                                                 request.GET.get('day_hour_restore')),
                                                             hours=hours, active=False)
                print(hour_to_disable)
                hour_to_disable.active = True
                hour_to_disable.save()
                response = {'status': '200', 'reason': 'Hai riattivato la fascia ' + str(
                    hours.start_hour.strftime('%H:%M')) + ' - ' + str(
                    hours.end_hour.strftime('%H:%M')) + ' per il giorno ' + str(
                    course_day_hours.get_day_display()) + ''}
                return JsonResponse(response, safe=False, content_type='application/json')
            except Exception as e:
                print(e)
                response = {'status': '500', 'reason': 'Si è verificato un errore.'}
                return JsonResponse(response, safe=False, content_type='application/json')
        raise PermissionDenied
