from django import forms
from django.contrib.auth import password_validation
from django.utils.translation import gettext_lazy as _

from core.auth.permissions import CustomManagement
from core.models import CustomUser, Sex


class RegisterForm(forms.ModelForm):
    error_messages = {
        'password_mismatch': _('Le password inserite non corrispondono.'),
    }

    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control mb-2','form':'register_form'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control mb-2','form':'register_form'}),
        strip=False,
        help_text=_("Inserisci la stessa password di sopra, per la verifica."),
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control mb-2','form':'register_form'}),
    )

    address = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control mb-2','form':'register_form'}),
        label='Indirizzo di abitazione')

    # cap = forms.CharField(
    #     error_messages={'Errore':'Il cap deve essere lungo 5 cifre'},
    #     help_text='Il cap deve essere lungo 5 cifre' ,
    #     widget=forms.TextInput(attrs={'class': 'form-control mb-2'}),
    #                            label ='CAP',max_length=5)
    phone = forms.CharField(
        error_messages={'Errore': 'Il numero di telefono inserito non è corretto'},
        widget=forms.TextInput(attrs={'class': 'form-control mb-2','form':'register_form', 'type':'number'}),
        help_text='Il numero di telefono deve essere lungo 10 cifre',
        label='Telefono'
    )
    # mobile_phone = forms.CharField(
    #     error_messages={'Errore': 'Il numero di cellulare inserito non è corretto'},
    #     widget=forms.TextInput(attrs={'class': 'form-control mb-2'}),
    #     label='Cellulare'
    # )

    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control mb-2','form':'register_form', 'type': 'date'}, format='%Y-%m-%d'),
        label='Data di Nascita')
    sex = forms.ModelChoiceField(queryset=Sex.objects.all(), widget=forms.Select(attrs={'class': 'form-control mb-2','form':'register_form'}),
                                 label='Sesso')
    town = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-2','form':'register_form'}), label='Città')
    town_birth = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-2','form':'register_form'}), label='Città di nascita')
    # state = forms.ModelChoiceField(queryset=States.objects.all(), widget=forms.Select(attrs={'class':'form-control mb-2'}), label='Paese')
    codice_fiscale = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-2','form':'register_form'}),
                                     label='Codice Fiscale', max_length=16)

    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'phone', 'address',
                  'sex', 'date_of_birth', 'town', 'codice_fiscale','town_birth')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control mb-2', 'form':'register_form'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control mb-2','form':'register_form'}),
            'email': forms.EmailInput(attrs={'class': 'form-control mb-2','form':'register_form'}),
            'phone': forms.TextInput(attrs={'class': 'form-control mb-2','form':'register_form'}),
            'address': forms.TextInput(attrs={'class': 'form-control mb-2','form':'register_form'}),
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

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        print(self.cleaned_data['username'])
        user.save()
        if commit:
            manageGroup = CustomManagement()
            manageGroup.set_group_to_user(group='utente', user=self.cleaned_data['username'], app_label='core',
                                          model='CustomUser')
        return user
