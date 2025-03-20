from django.urls import path
from . import views

urlpatterns = [
    path('liste_evernement', views.liste_evenements, name='liste_evenements'),
    path('<int:evenement_id>/', views.detail_evenement, name='detail_evenement'),
    path('ajouter/', views.ajouter_evenement, name='ajouter_evenement'),
    path('modifier/<int:evenement_id>/', views.modifier_evenement, name='modifier_evenement'),
    path('supprimer/<int:evenement_id>/', views.supprimer_evenement, name='supprimer_evenement'),
]
