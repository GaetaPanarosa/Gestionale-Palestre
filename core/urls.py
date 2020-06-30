from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

from control_panel.views import PrenotationManagementAdmin
from core.auth.views import LogoutView
from core.views.general_views import FormsetCreator
from core.views.user_views import UserProfile
from gestionale_palestre import settings
from user_panel.views.prenotation.prenotation_views import PrenotationManagement

urlpatterns = [
    path('', include('website.urls')),
    path('control_panel/', include('control_panel.urls'), name='control_panel'),
    path('pannello_utente/', include('user_panel.urls'), name='index_user'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create_form_set/', FormsetCreator.create_formset, name='formset_creator'),
    path('get_hours_for_prenotation/', PrenotationManagement.get_hours, name="get_hours_for_prenotation"),
    path('get_hours/', PrenotationManagementAdmin.get_hours, name="get_hours"),
    path('prenotazione', PrenotationManagement.prenotation, name="prenotation_submit"),
    path('check_hours/', PrenotationManagement.check_disponibility, name="check_disponibility"),
    path('check/', PrenotationManagementAdmin.check_disponibility, name="check"),
    path('profile/', UserProfile.as_view(template_name='core/profile.html'), name='profile')
    ]

urlpatterns += static (settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
urlpatterns += staticfiles_urlpatterns ()