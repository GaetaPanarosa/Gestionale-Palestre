import json

from django.core.exceptions import PermissionDenied
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from core.forms import HoursForm
from core.models import Hours


class HoursManagement(TemplateView):
    form_class = HoursForm
    template_name = 'hours/hours.html'

    def get(self, request, *args, **kwargs):
        hours = Hours.objects.all().order_by('start_hour').order_by('end_hour')
        return render(request, self.template_name, {'form_hours': self.form_class, 'hours': hours})

    def post(self, request, *args, **kwargs):
        print(request.POST)
        data = json.dumps(request.POST)
        print(data)
        if request.is_ajax and request.method == 'POST':
            form_hours = HoursForm(request.POST)
            if form_hours.is_valid():
                hours = Hours.objects.filter(start_hour=form_hours.cleaned_data['start_hour'],
                                             end_hour=form_hours.cleaned_data['end_hour'])
                if not hours.exists():
                    if form_hours.cleaned_data['start_hour'] > form_hours.cleaned_data['end_hour']:
                        response = {'status': '500',
                                    'reason': 'L\'orario di inizio non può essere successivo all\'orario di fine.'}
                        return JsonResponse(response, safe=False, content_type="application/json")
                    form_hours.save()
                    response = {'status': '200', 'reason': 'Fascia oraria inserita con successo.'}
                    return JsonResponse(response, safe=False, content_type="application/json")
                response = {'status': '500', 'reason': 'Questa fascia oraria esiste già.'}
                return JsonResponse(response, safe=False, content_type="application/json")
            response = {'status': '500', 'reason': 'Si è verificato un errore durante l\'inserimento.'}
            return JsonResponse(response, safe=False, content_type="application/json")

    def mod_hours(request, pk):
        print(request)
        if request.method == 'POST':
            try:
                if request.POST.get('start_hour') > request.POST.get('end_hour'):
                    response = {'status': '500',
                                'reason': 'L\'orario di inizio non può essere successivo all\'orario di fine.'}
                    return JsonResponse(response, safe=False, content_type="application/json")
                forms_hours_mod = Hours.objects.get(pk=pk)
                forms_hours_mod.start_hour = request.POST.get('start_hour')
                forms_hours_mod.end_hour = request.POST.get('end_hour')
                forms_hours_mod.save()
                response = {'status': '200', 'reason': 'Fascia oraria modificata con successo.'}
                return JsonResponse(response, safe=False, content_type="application/json")
            except:
                response = {'status': '500', 'reason': 'Si è verificato un errore durante l\'inserimento.'}
                return JsonResponse(response, safe=False, content_type="application/json")
        raise PermissionDenied

    def del_hours(request, pk):
        if request.method == 'GET':
            try:
                print(request.GET)
                print(pk)
                Hours.objects.get(pk=pk).delete()
                response = {'status': '200', 'reason': 'Fascia oraria eliminata.'}
                return JsonResponse(response, safe=False, content_type="application/json")
            except Exception as e:
                print(e)
                response = {'status': '500', 'reason': 'Si è verificato un errore durante l\'inserimento.'}
                return JsonResponse(response, safe=False, content_type="application/json")
        raise PermissionDenied

    def info(request, pk):
        print(pk)
        hours_info = Hours.objects.get(pk=pk)
        response = {'status': 'ok', 'start_hour': hours_info.start_hour, 'end_hour': hours_info.end_hour,
                    'pk': hours_info.pk}
        return JsonResponse(response, safe=False, content_type='application/json')
