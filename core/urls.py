from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

from core.auth import *
from core.views import *
from gestionale_palestre import settings

urlpatterns = [
    path('', include('website.urls'), name='website'),
    path('corsi/', include('course.urls'), name="corsi"),
    path('control_panel/', include('control_panel.urls'), name='control_panel'),
    path('prenotazioni/', include('prenotation.urls'), name='prenotations'),
    path('istruttore/', include('trainer.urls')),
    # path('pannello_utente/', include('user.urls'), name='index_user'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # path('create_form_set/', FormsetCreator.create_formset, name='formset_creator'),
    # path('check_hours/', PrenotationManagement.check_disponibility, name="check_disponibility"),
    # path('check/', PrenotationManagementAdmin.check_disponibility, name="check"),
    path('profilo/', UserProfile.as_view(), name='profile'),

    # URL Fasce orarie
    path('fasce_orarie_corso', HoursManagement.as_view(), name="hours_course"),
    path('fasce_orarie', HoursManagement.as_view(), name="hours"),
    path('info_fascia/<int:pk>/', HoursManagement.info, name="hours_info"),
    path('modifica_fasce/<int:pk>/', HoursManagement.mod_hours, name="mod_hours"),
    path('cancella_fascia/<int:pk>/', HoursManagement.del_hours, name="del_hours"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
urlpatterns += staticfiles_urlpatterns()
