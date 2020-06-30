from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic import TemplateView

from user_panel.views import UserIndex
from user_panel.views.prenotation.prenotation_views import PrenotationManagement, PrenotationUserTable

urlpatterns = [
    path('', login_required(UserIndex.as_view(template_name='user_panel/base_user_panel/index.html'), redirect_field_name=''), name='index_user'),
    path('prenotazione/',login_required(PrenotationManagement.as_view(template_name='user_panel/prenotation/prenotation.html'),redirect_field_name=''), name='prenotation'),
    path('le_mie_prenotazioni/',login_required(TemplateView.as_view(template_name='user_panel/prenotation/user_prenotations.html'),redirect_field_name=''), name='prenotation_users'),
    path('dismiss_prenotation/',login_required(PrenotationManagement.dismiss_prenotation,redirect_field_name=''), name='prenotation_dismiss'),
    path('prenotazioni_utente_table/',PrenotationUserTable.as_view(), name='prenotation_table'),
]
