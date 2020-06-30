from django.http import JsonResponse
from django.shortcuts import render

from core.forms.users.register import RegisterForm
from website.views.template import NavbarTemplate


class Register(NavbarTemplate):
    template_name = 'website/base_templates/registrazione.html'
    print('Entrato Registrazione')

    def get(self, request, *args, **kwargs):
        form_class = RegisterForm
        return render(request, self.template_name, {'form': form_class, 'form_login': NavbarTemplate.form_class })

    def post(self, request, *args, **kwargs):
        print(self.request.POST)
        form_class = RegisterForm(request.POST)

        if form_class.is_valid():
            form_class.save()
            # data = {'username': request.POST.get('username'), 'password': CustomUser.objects.get(username= request.POST.get('username')).password}
            data = {'username': form_class.cleaned_data['username'], 'password': form_class.cleaned_data['password1']}
            print(data)
            return JsonResponse({'status': '200', 'reason': 'Registrazione avvenuta con successo', 'data':data})
        else:
            return JsonResponse({'status': 'error', 'reason': [v[0] for k, v in form_class.errors.items()]}, safe=False,
                                content_type='application/json')

