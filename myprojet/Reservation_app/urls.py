from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('reservation/creer/', reservation_view, name='creer_reservation'),
    path("liste_reservation/", reservation_list, name="liste_reservation"),
    path('reservation/update/<int:reservation_id>/', views.update_reservation, name='update_reservation'),
    path('reservation/delete/<int:reservation_id>/', views.delete_reservation, name='delete_reservation'),
]

