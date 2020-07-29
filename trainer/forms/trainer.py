from django import forms

from trainer.models import Trainer, TrainerType


class TrainerForm(forms.ModelForm):
    disponibility = forms.ChoiceField(
        widget=forms.CheckboxInput(attrs={'class': 'input-sm form-control-sm', 'form': 'form_trainer'}),
        label='Disponibilità')
    type = forms.ModelChoiceField(queryset=TrainerType.objects.filter(active=True), widget=forms.Select(
        attrs={
            'class': 'form-control select2-single select2-hidden-accessible',
            'data-width': '100%',
            'form': 'form_trainer',
            'placeholder': 'Scegli tipologia istruttore',
            'readonly': 'readonly'
        }), required=True)
    # price = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control', 'form': 'form_trainer', 'placeholder': '0.0€'}))
    class Meta:
        model = Trainer
        fields = ['disponibility','type']
