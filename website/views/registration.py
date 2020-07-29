from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.shortcuts import render, redirect

from core.forms.users.register import RegisterForm
from website.views.template import NavbarTemplate


class Register(NavbarTemplate):
    template_name = 'base_templates/registrazione.html'
    print('Entrato Registrazione')

    def get(self, request, *args, **kwargs):
        form_class = RegisterForm
        return render(request, self.template_name, {'form': form_class, 'form_login': NavbarTemplate.form_class})

    def post(self, request, *args, **kwargs):
        print(self.request.POST)
        form_class = RegisterForm(request.POST)

        if form_class.is_valid():
            form_class.save()
            user = authenticate(request, username=form_class.cleaned_data['username'],
                                password=form_class.cleaned_data['password1'])
            if user is not None:
                # return JsonResponse({'status': '200', 'reason': 'Registrazione avvenuta con successo. Verrai reindirizzato alla tua pagina personale.'})
                return redirect('/user_panel/')
            else:
                return JsonResponse({'status': '500',
                                     'reason': 'Si è verificato un errore durante il login automatico. Ti preghiamo di utilizzare l\'apposita funzione per effettuare l\'accesso.'})
        else:
            return JsonResponse({'status': 'error', 'reason': [v[0] for k, v in form_class.errors.items()]}, safe=False,
                                content_type='application/json')
