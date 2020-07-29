from django import forms
from django.contrib.auth import password_validation
from django.utils.translation import gettext_lazy as _

from core.models import CustomUser, Sex


class ProfileForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control mb-2', 'form': 'profile_form'}),
    )

    address = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'form': 'profile_form'}),
        label='Indirizzo di abitazione')

    phone = forms.CharField(
        error_messages={'Errore': 'Il numero di telefono inserito non è corretto'},
        widget=forms.TextInput(attrs={'class': 'form-control', 'form': 'profile_form', 'type': 'number'}),
        help_text='Il numero di telefono deve essere lungo 10 cifre',
        label='Telefono'
    )

    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control datepicker', 'form': 'profile_form', 'type': 'date'},
                               format='%Y-%m-%d'),
        label='Data di Nascita')
    sex = forms.ModelChoiceField(queryset=Sex.objects.all(),
                                 widget=forms.Select(
                                     attrs={'class': 'form-control select2-single select2-hidden-accessible',
                                            'tab-index': '-1', 'data-width': '100%', 'form': 'profile_form'}),
                                 label='Sesso')
    town = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'form': 'profile_form'}),
                           label='Città')
    town_birth = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'form': 'profile_form'}),
                                 label='Città di nascita')

    codice_fiscale = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'form': 'profile_form'}),
        label='Codice Fiscale', max_length=16)

    class Meta:
        model = CustomUser

        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'date_of_birth',
            'codice_fiscale',
            'town',
            'town_birth',
            'phone',
            'address',
            'sex',
            'image'
        ]

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control mb-2', 'form': 'profile_form'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control mb-2', 'form': 'profile_form'}),
            'email': forms.EmailInput(attrs={'class': 'form-control mb-2', 'form': 'profile_form'}),
            'phone': forms.TextInput(attrs={'class': 'form-control mb-2', 'form': 'profile_form'}),
            'address': forms.TextInput(attrs={'class': 'form-control mb-2', 'form': 'profile_form'}),
        }


class AccountForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'form': 'account_form'}),
    )
    error_messages = {
        'password_mismatch': _('Le password inserite non corrispondono.'),
    }

    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password', 'class': 'form-control mb-2', 'form': 'register_form'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password', 'class': 'form-control mb-2', 'form': 'register_form'}),
        strip=False,
        help_text=_("Inserisci la stessa password di sopra, per la verifica."),
    )

    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}))

    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'image']
