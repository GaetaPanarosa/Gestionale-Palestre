from django import forms

from core.models import Hours
from course.models import Trainer, Course, CourseDay


class CourseForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'form': 'add_course_id', 'placeholder': 'Nome del corso'}),
                           required=True)
    description = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'form': 'add_course_id', 'placeholder': 'Descrizione del corso'}))
    min_subscribers = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'form': 'add_course_id', 'placeholder': '1', 'min': '1'}), required=True)
    max_subscribers = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'form': 'add_course_id', 'placeholder': '1', 'min': '1'}), required=True)
    # n_max_subscribers = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control', 'form':'add_course_id', 'placeholder':''}), required=True)
    price = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'form': 'add_course_id', 'placeholder': '40€'}),
        required=False)
    start_date = forms.DateField(
        widget=forms.DateInput(
            attrs={'class': 'form-control datepicker', 'data-date-format': 'dd/mm/yyyy', 'form': 'add_course_id',
                   'readonly': 'readonly', 'type': 'text', 'placeholder': ''}))
    end_date = forms.DateField(
        widget=forms.DateInput(
            attrs={'class': 'form-control datepicker', 'data-date-format': 'dd/mm/yyyy', 'form': 'add_course_id',
                   'readonly': 'readonly', 'placeholder': ''}))
    trainer = forms.ModelChoiceField(queryset=Trainer.objects.filter(details__groups__name='trainer'),
                                     widget=forms.Select(
                                         attrs={
                                             'class': 'form-control select2-single select2-hidden-accessible',
                                             'data-width': '100%',
                                             'form': 'add_course_id',
                                             'placeholder': 'Scegli',
                                             'readonly': 'readonly'
                                         }),
                                     required=False)

    class Meta:
        model = Course
        fields = [
            'name',
            'description',
            'min_subscribers',
            'max_subscribers',
            'price',
            'start_date',
            'end_date',
            'trainer',
        ]


class CourseDayForm(forms.ModelForm):
    WEEK = (
        (0, 'Lunedi'),
        (1, 'Martedi'),
        (2, 'Mercoledì'),
        (3, 'Giovedì'),
        (4, 'Venerdì'),
        (5, 'Sabato'),
        (6, 'Domenica'),
    )
    course = forms.ModelChoiceField(queryset=Course.objects.filter(active=True), widget=forms.Select(
        attrs={'class': 'form-control select2-single select2-hidden-accessible', 'data-width': '100%',
               'form': 'add_course_day_hours', 'data-placeholder': 'Seleziona corso', 'readonly': 'readonly'}))
    day = forms.ChoiceField(choices=WEEK, widget=forms.Select(
        attrs={'class': 'form-control select2-single select2-hidden-accessible', 'data-width': '100%',
               'form': 'add_course_day_hours', 'data-placeholder': 'Seleziona giorno', 'readonly': 'readonly'}))

    hours = forms.ModelMultipleChoiceField(queryset=Hours.objects.filter(active=True).order_by('start_hour'),
                                           widget=forms.SelectMultiple(
                                               attrs={'class': 'form-control select2-single',
                                                      'form': 'add_course_day_hours', 'readonly': 'readonly',
                                                      'placeholder': 'Seleziona fasce', 'data-width': '100%'}, ))

    class Meta:
        model = CourseDay
        fields = ['course', 'day', 'hours']


class ModifyCourseForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'form': 'add_course_id'}),
                           required=True)
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'form': 'add_course_id'}))
    min_subscribers = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'form': 'add_course_id'}), required=True)
    max_subscribers = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'form': 'add_course_id'}), required=True)
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'form': 'add_course_id'}),
                               required=False)
    start_date = forms.DateField(
        widget=forms.DateInput(
            attrs={'class': 'form-control datepicker', 'data-date-format': 'dd/mm/yyyy', 'form': 'add_course_id',
                   'readonly': 'readonly'}))
    end_date = forms.DateField(
        widget=forms.DateInput(
            attrs={'class': 'form-control datepicker', 'data-date-format': 'dd/mm/yyyy', 'form': 'add_course_id',
                   'readonly': 'readonly'}))
    trainer = forms.ModelChoiceField(queryset=Trainer.objects.filter(details__groups__name='istruttore'),
                                     widget=forms.Select(
                                         attrs={
                                             'class': 'form-control select2-single select2-hidden-accessible',
                                             'data-width': '100%',
                                             'form': 'add_course_id',
                                             'placeholder': 'Scegli',
                                             'readonly': 'readonly'
                                         }),
                                     required=False)

    class Meta:
        model = Course
        fields = [
            'name',
            'description',
            'min_subscribers',
            'max_subscribers',
            'price',
            'start_date',
            'end_date',
            'trainer',
        ]
