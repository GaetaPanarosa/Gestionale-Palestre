from django import forms

from core.models import Hours


class HoursForm (forms.ModelForm):

    start_hour = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control','type':'time','form':'hours_form'}),label='Ora di inizio')
    end_hour = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control','type':'time','form':'hours_form'}),label='Ora di fine')

    class Meta:
        model = Hours
        fields = ['start_hour', 'end_hour']