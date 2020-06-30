from django.urls import path

from core.auth.views import *
from website.views import *

urlpatterns = [
    path('', NavbarTemplate.as_view(template_name='website/base_templates/index.html'), name='index'),
    path('login', LoginView.as_view(), name="login"),
    path('registrazione', Register.as_view(template_name='website/base_templates/registrazione.html'), name="register"),
    path('accounts/password_reset/', PasswordResetView.as_view(), name='reset_password'),
    path('accounts/password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/reset/done/', PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
