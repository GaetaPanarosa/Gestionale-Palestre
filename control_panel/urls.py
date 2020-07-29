from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic import TemplateView

from control_panel.views import AdminPanelNavbar, UserTable

urlpatterns = [
    path('', login_required(AdminPanelNavbar.as_view(), redirect_field_name=''), name='index_admin'),
    # URL Iscritti
    path('lista_iscritti/', TemplateView.as_view(template_name='users/users.html'),
         name="users_list"),
    path('lista_iscritti/iscritti_table/', UserTable.as_view(), name="user_table"),

]
