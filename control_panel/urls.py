from django.contrib.auth.decorators import login_required
from django.urls import path

from control_panel.views import AdminPanelNavbar
from control_panel.views.course_views import *
from control_panel.views.hours_views import HoursManagement
from control_panel.views.prenotation_views import *
from control_panel.views.trainer_views import TrainerRegister
from control_panel.views.users_view import UserTable

urlpatterns = [
    path('', login_required(AdminPanelNavbar.as_view(template_name='control_panel/base_control_panel/index.html'), redirect_field_name=''), name='index_admin'),
    # URL corso
    path('corsi/', login_required(CourseManagement.as_view(template_name='control_panel/course/courses.html'),redirect_field_name=''),name='courses'),
    path('corsi_disattivati/', login_required(CourseManagement.as_view(template_name='control_panel/course/courses_disactivated.html'),redirect_field_name=''),name='courses_disactivated'),
    path('corsi/course_table/', CourseTable.as_view(), name='course_table'),
    path('corsi/course_disactivated_table/', CourseDisactivatedTable.as_view(), name='course_disactivated_table'),
    path('aggiungi_corso/', login_required(CourseManagement.as_view(template_name='control_panel/course/new_course.html'), redirect_field_name=''), name='nuovo_corso'),
    path('corso_giorno_ora', login_required(CourseDayHoursView.as_view(), redirect_field_name=''), name='course_m2m'),
    path('disattiva_corso/', login_required(CourseManagement.disactiveCourse, redirect_field_name=''), name="disactive_course"),
    path('riattiva_corso/', login_required(CourseManagement.enableCourse, redirect_field_name=''), name="enable_course"),
    path('disattiva_fascia_corso/', login_required(CourseDayHoursView.disableHourFromCourse, redirect_field_name=''), name='disactive_hours_from_course'),
    path('disattiva_giorno_corso/', login_required(CourseManagement.disableDay, redirect_field_name=''), name='disactive_day'),
    path('riattiva_giorno_corso/', login_required(CourseManagement.restoreDay, redirect_field_name=''), name='restore_day'),
    path('riattiva_fascia_corso/', login_required(CourseDayHoursView.restore_hours_for_day, redirect_field_name=''), name='restore_hours_from_course'),
    path('corsi/dettaglio_corso/<int:pk>/',login_required(CourseManagement.details_course, redirect_field_name=''), name="details_course"),
    # URL istruttore
    path('aggiungi_istruttore/', TrainerRegister.as_view(), name='nuovo_istruttore'),

    # URL Fasce orarie
    path('fasce_orarie_corso', HoursManagement.as_view(), name="hours_course"),
    path('fasce_orarie', HoursManagement.as_view(template_name='control_panel/hours/hours.html'), name="hours"),
    path('info_fascia/<int:pk>/', HoursManagement.info, name="hours_info"),
    path('modifica_fasce/<int:pk>/', HoursManagement.mod_hours, name="mod_hours"),
    path('cancella_fascia/<int:pk>/', HoursManagement.del_hours, name="del_hours"),

    # URL Prenotazioni
    path('prenotazioni/', PrenotationManagementAdmin.as_view(template_name='control_panel/prenotation/prenotation.html'), name="prenotation_list"),
    path('prenotazioni/dettaglio_prenotazione/<str:pk>/', PrenotationDetails.as_view(template_name='control_panel/prenotation/prenotation_details.html'), name="prenotation_details"),
    # path('prenotazioni/dettaglio_prenotazione/<str:pk>/', PrenotationDetails, name="mod_prenotation"),
    path('prenotation/prenotation_table/', PrenotationTable.as_view(), name="prenotation_table"),
    path('prenotation/prenotation_table_details/<int:course>/<str:pk>/<str:date>/', PrenotationDetailsTable.as_view(), name="prenotation_table_details"),

    # URL Iscritti
    path('lista_iscritti/', TemplateView.as_view(template_name='control_panel/users/users.html'),
         name="users_list"),
    path('lista_iscritti/iscritti_table/', UserTable.as_view(), name="user_table"),

]
