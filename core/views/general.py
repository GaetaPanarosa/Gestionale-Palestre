from datetime import datetime, timedelta

from django.http import JsonResponse
from django.views.generic import TemplateView

from course.models import CourseDayHours


class FormsetCreator(TemplateView):
    def create_formset(request):
        course = CourseDayHours.objects.filter(pk=int(request.GET.get('pk'))).first()
        hours = list()
        for h in course.hours.all().filter(start_hour__gte=datetime.now() + timedelta(hours=2)):
            hours.append(
                {'id': h.pk, 'start_hour': h.start_hour.strftime('%H:%M'), 'end_hour': h.end_hour.strftime('%H:%M')})
        print(len(hours))
        return JsonResponse(hours, safe=False, content_type='application/json')
