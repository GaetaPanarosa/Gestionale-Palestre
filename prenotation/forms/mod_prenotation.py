from django import forms

from core.models import Hours
from course.models import Course
from prenotation.models.prenotations import Prenotation


class ModPrenotationForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(
            attrs={'class': 'form-control datepicker', 'data-date-format': 'dd/mm/yyyy', 'form': 'mod_prenotation',
                   'readonly': 'readonly'}))

    course = forms.ModelChoiceField(queryset=Course.objects.filter(active=True), widget=forms.Select(
        attrs={'class': 'form-control select2-single select2-hidden-accessible', 'data-width': '100%',
               'form': 'mod_prenotation', 'data-placeholder': 'Seleziona corso', 'readonly': 'readonly'}))

    time = forms.ModelChoiceField(queryset=Hours.objects.filter(active=True).order_by('start_hour'),
                                  widget=forms.Select(
                                      attrs={'class': 'form-control select2-single select2-hidden-accessible',
                                             'data-width': '100%',
                                             'form': 'mod_prenotation', 'data-placeholder': 'Seleziona fascia oraria',
                                             'readonly': 'readonly'}))

    user = forms.HiddenInput()

    active = forms.CharField(widget=forms.CheckboxInput())

    class Meta:
        model = Prenotation
        fields = [
            'course', 'date', 'user', 'active', 'time'
        ]
