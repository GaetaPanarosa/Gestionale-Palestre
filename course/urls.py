from django.contrib.auth.decorators import login_required
from django.urls import path

from course.views import *
from course.views import CourseTable, CourseDisactivatedTable

urlpatterns = [
    # URL corso
    path('',
         login_required(CourseManagement.as_view(template_name='courses.html'),
                        redirect_field_name=''), name='courses'),
    path('corsi_disattivati/', login_required(
        CourseManagement.as_view(template_name='courses_disactivated.html'),
        redirect_field_name=''), name='courses_disactivated'),
    path('course_table/', CourseTable.as_view(), name='course_table'),
    path('course_disactivated_table/', CourseDisactivatedTable.as_view(), name='course_disactivated_table'),
    path('aggiungi_corso/', login_required(
        CourseManagement.as_view(template_name='new_course.html'),
        redirect_field_name=''), name='nuovo_corso'),
    path('corso_giorno_ora', login_required(CourseDayHoursView.as_view(), redirect_field_name=''), name='course_m2m'),
    path('disattiva_corso/', login_required(CourseManagement.disactiveCourse, redirect_field_name=''),
         name="disactive_course"),
    path('riattiva_corso/', login_required(CourseManagement.enableCourse, redirect_field_name=''),
         name="enable_course"),
    path('disattiva_fascia_corso/', login_required(CourseDayHoursView.disableHourFromCourse, redirect_field_name=''),
         name='disactive_hours_from_course'),
    path('disattiva_giorno_corso/', login_required(CourseManagement.disableDay, redirect_field_name=''),
         name='disactive_day'),
    path('riattiva_giorno_corso/', login_required(CourseManagement.restoreDay, redirect_field_name=''),
         name='restore_day'),
    path('riattiva_fascia_corso/', login_required(CourseDayHoursView.restore_hours_for_day, redirect_field_name=''),
         name='restore_hours_from_course'),
    path('dettaglio_corso/<int:pk>/', login_required(CourseManagement.details_course, redirect_field_name=''),
         name="details_course"),
    path('course_settings',
         login_required(TemplateView.as_view(template_name='course_settings.html'), redirect_field_name=''),
         name="course_settings"),
]
