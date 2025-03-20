from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'menu'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('accounts/profile/', views.logout_view, name='profile'),
    path('menus/', views.MenuListView.as_view(), name='liste_menus'),
    # Détails d'un menu
    path('<int:pk>/', views.MenuDetailView.as_view(), name='detail_menu'),
    # Créer un nouveau menu
    path('creer/', views.MenuCreateView.as_view(), name='creer_menu'),
    # Modifier un menu
    path('<int:pk>/modifier/', views.MenuUpdateView.as_view(), name='modifier_menu'),
    # Supprimer un menu
    path('<int:pk>/supprimer/', views.MenuDeleteView.as_view(), name='supprimer_menu'),
    path('table/', views.create_table, name="create_table"),
    path('liste_table/', views.list_table, name="liste_table"),
    path('edit/<int:table_id>/', views.edit_table, name='edit_table'),
    path('delete/<int:table_id>/', views.delete_table, name='delete_table'),
    path('service/', views.service, name="service"),
    path('contact/', views.ContactCreateView.as_view(), name="create_contact"),
    path('liste_contact/', views.ContactListView.as_view(), name="liste_contact"),
]
