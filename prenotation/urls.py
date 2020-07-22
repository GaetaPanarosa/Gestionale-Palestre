from django.urls import path

from prenotation.views.admin import PrenotationManagementAdmin, PrenotationDetails, PrenotationTable, \
    PrenotationDetailsTable

urlpatterns = [
    # URL Prenotazioni
    path('prenotazioni/',
         PrenotationManagementAdmin.as_view(template_name='control_panel/prenotation/prenotation.html'),
         name="prenotation_list"),
    path('prenotazioni/dettaglio_prenotazione/<str:pk>/',
         PrenotationDetails.as_view(template_name='control_panel/prenotation/prenotation_details.html'),
         name="prenotation_details"),
    # path('prenotazioni/dettaglio_prenotazione/<str:pk>/', PrenotationDetails, name="mod_prenotation"),
    path('prenotation/prenotation_table/', PrenotationTable.as_view(), name="prenotation_table"),
    path('prenotation/prenotation_table_details/<int:course>/<str:pk>/<str:date>/', PrenotationDetailsTable.as_view(),
         name="prenotation_table_details"),
]
