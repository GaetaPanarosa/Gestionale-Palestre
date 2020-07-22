from django.urls import path

from trainer.views.register import TrainerRegister

urlpatterns = [
    path('aggiungi_istruttore/', TrainerRegister.as_view(), name='nuovo_istruttore'),
]
