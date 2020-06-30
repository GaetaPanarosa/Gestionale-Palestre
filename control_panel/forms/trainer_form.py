from django import forms
from django.contrib.auth import password_validation
from django.utils.translation import gettext_lazy as _

from core.models import Trainer, Sex, CustomUser


class TrainerForm(forms.ModelForm):
    disponibility = forms.ChoiceField(widget=forms.CheckboxInput(attrs={'class': 'input-sm form-control-sm','form':'form_trainer'}),
                                      label='Disponibilità')
    class Meta:
        model = Trainer
        fields = ['disponibility']

class TrainerFormRegister(forms.ModelForm):
    error_messages = {
        'password_mismatch': _('Le password inserite non corrispondono.'),
    }

    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password', 'class': 'form-control mb-2', 'form': 'form_trainer'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password', 'class': 'form-control mb-2', 'form': 'form_trainer'}),
        strip=False,
        help_text=_("Inserisci la stessa password di sopra, per la verifica."),
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control mb-2', 'form': 'form_trainer'}),
    )

    address = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control mb-2', 'form': 'form_trainer'}),
        label='Indirizzo di abitazione')

    phone = forms.CharField(
        error_messages={'Errore': 'Il numero di telefono inserito non è corretto'},
        widget=forms.TextInput(attrs={'class': 'form-control mb-2', 'form': 'form_trainer'}),
        help_text='Il numero di telefono deve essere lungo 10 cifre',
        label='Telefono'
    )

    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control datepicker mb-2', 'form': 'form_trainer', 'data-date-format':'dd/mm/yyyy','readonly':'readonly'},
                               format='%Y-%m-%d'),
        label='Data di Nascita')
    sex = forms.ModelChoiceField(queryset=Sex.objects.all(),
                                 widget=forms.Select(attrs={'class': 'form-control select2-single mb-2', 'form': 'form_trainer'}),
                                 label='Sesso')
    town = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-2', 'form': 'form_trainer'}),
                           label='Città')
    town_birth = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control mb-2', 'form': 'form_trainer'}),
        label='Città di nascita')
    # state = forms.ModelChoiceField(queryset=States.objects.all(), widget=forms.Select(attrs={'class':'form-control mb-2'}), label='Paese')
    codice_fiscale = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control mb-2', 'form': 'form_trainer'}),
        label='Codice Fiscale', max_length=16)

    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'phone', 'address',
                  'sex', 'date_of_birth', 'town', 'codice_fiscale','town_birth')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control mb-2', 'form': 'form_trainer'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control mb-2', 'form': 'form_trainer'}),
            'email': forms.EmailInput(attrs={'class': 'form-control mb-2', 'form': 'form_trainer'}),
            'phone': forms.TextInput(attrs={'class': 'form-control mb-2', 'form': 'form_trainer'}),
            'address': forms.TextInput(attrs={'class': 'form-control mb-2', 'form': 'form_trainer'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self._meta.model.USERNAME_FIELD in self.fields:
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs['autofocus'] = True

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def _post_clean(self):
        super()._post_clean()
        # Validate the password after self.instance is updated with form data
        # by super().
        password = self.cleaned_data.get('password2')
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except forms.ValidationError as error:
                self.add_error('password2', error)

