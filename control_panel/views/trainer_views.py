import json

from django.core.exceptions import PermissionDenied
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from control_panel.forms.trainer_form import TrainerForm, TrainerFormRegister
from core.auth.permissions import CustomManagement
from core.forms.users import CustomUser
from core.models import Trainer


class TrainerRegister(TemplateView):
    form_trainer = TrainerForm
    form_trainer_user = TrainerFormRegister
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form_trainer': self.form_trainer, 'form_trainer_user':self.form_trainer_user})

    def post(self, request, *args, **kwargs):
        response = {}
        print(request.POST)
        data = json.dumps(request.POST)
        print(data)
        if request.is_ajax and request.method == 'POST':
            form_trainer_user = TrainerFormRegister(request.POST)
            if form_trainer_user.is_valid():
                form_trainer_user.save()
                manageGroup = CustomManagement()
                manageGroup.set_group_to_user(group='istruttore', user=request.POST.get('username'), app_label='core',
                                                  model='CustomUser')
                trainer = Trainer()
                if request.POST.get('disponibility') == 'on':
                    trainer.disponibility = True
                else:
                    trainer.disponibility = False
                trainer.details = CustomUser.objects.get(username=request.POST.get('username'),codice_fiscale=request.POST.get('codice_fiscale'))
                trainer.save()
                print('valido')
                response = {'status':'200','reason':'Inserimento dell\'istruttore riuscito correttamente'}
                return JsonResponse(response, safe=False, content_type="application/json")
                # except Exception as e:
                #     return JsonResponse(str(e), safe=False, content_type='application/json')
            response = {'status': '500', 'reason': 'Si è verificato un errore'}
            return JsonResponse({'status': 'error', 'reason': [v[0] for k, v in form_trainer_user.errors.items()]}, safe=False,
                                content_type='application/json')

        else:
            raise PermissionDenied
