from django import forms

from core.models import Prenotation, Course


class PrenotationForm(forms.ModelForm):

    course = forms.ModelChoiceField(required=True, queryset=Course.objects.filter(active =True), widget=forms.Select(attrs={'class':'form-control','form':'prenotation_form'}))


    class Meta:
        model = Prenotation
        fields = ['course']

    def __init__(self, *args, **kwargs):
        if kwargs.get('instance'):
            initial = kwargs.setdefault('initial', {})
            initial['course'] = [t.pk for t in kwargs['course'].hours_set.all()]

        forms.ModelForm.__init__(self, *args, **kwargs)

