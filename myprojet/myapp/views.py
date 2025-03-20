from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Contact, Menu, Evenement, Table
from .forms import ContactForm, MenuForm, EvenementForm, TableForm
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator


# Fonction pour vérifier si l'utilisateur est un administrateur
def is_admin(user):
    return user.is_superuser

# Accueil
def home(request):
    return render(request, 'home.html')

# Inscription
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu:login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# Connexion
def login_view(request):
    next_url = request.GET.get('next')  # Pran URL itilizatè te eseye ale a
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            
            # 🔹 Sèvi ak `next_url` si li egziste, sinon voye l nan `menu:home`
            return redirect(next_url if next_url else 'menu:home')
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def profile_view(request):
    return render(request, 'profile.html', {'user': request.user})

# Déconnexion
def logout_view(request):
    if request.method == 'POST':
        logout(request)
    return redirect('menu:home')

# Views pour Contact
class ContactListView(ListView):
    model = Contact
    template_name = 'liste_contacts.html'
    context_object_name = 'contacts'

class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = reverse_lazy('menu:liste_contact')
    context_object_name = 'contact'

class ContactUpdateView(UpdateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact/modifier_contact.html'
    success_url = reverse_lazy('liste_contacts')

class ContactDeleteView(DeleteView):
    model = Contact
    template_name = 'contact/supprimer_contact.html'
    success_url = reverse_lazy('liste_contacts')

class ContactDetailView(DetailView):
    model = Contact
    template_name = 'contact/detail_contact.html'

# Views pour Menu
class MenuListView(ListView):
    model = Menu
    template_name = 'menu/liste_menus.html'
    context_object_name = 'menus'

def is_admin(user):
    return user.is_superuser

# Vue pour créer un menu
@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(is_admin), name='dispatch')
class MenuCreateView(CreateView):
    model = Menu
    form_class = MenuForm
    template_name = 'menu/creer_menu.html'
    success_url = reverse_lazy('menu:liste_menus')

# Vue pour modifier un menu
@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(is_admin), name='dispatch')
class MenuUpdateView(UpdateView):
    model = Menu
    form_class = MenuForm
    template_name = 'menu/modifier_menu.html'
    success_url = reverse_lazy('menu:liste_menus')

# Vue pour supprimer un menu
@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(is_admin), name='dispatch')
class MenuDeleteView(DeleteView):
    model = Menu
    template_name = 'menu/supprimer_menu.html'
    success_url = reverse_lazy('menu:liste_menus')

class MenuDetailView(DetailView):
    model = Menu
    template_name = 'menu/detail_menu.html'

# Views pour Evenement
class EvenementListView(ListView):
    model = Evenement
    template_name = 'evenement/liste_evenements.html'
    context_object_name = 'evenements'

@login_required
@user_passes_test(is_admin)
class EvenementCreateView(CreateView):
    model = Evenement
    form_class = EvenementForm
    template_name = 'evenement/creer_evenement.html'
    success_url = reverse_lazy('liste_evenements')

@login_required
@user_passes_test(is_admin)
class EvenementUpdateView(UpdateView):
    model = Evenement
    form_class = EvenementForm
    template_name = 'evenement/modifier_evenement.html'
    success_url = reverse_lazy('liste_evenements')

class EvenementDeleteView(DeleteView):
    model = Evenement
    template_name = 'evenement/supprimer_evenement.html'
    success_url = reverse_lazy('liste_evenements')

class EvenementDetailView(DetailView):
    model = Evenement
    template_name = 'evenement/detail_evenement.html'

# Fonction pour créer une table, accessible uniquement aux administrateurs
@login_required
@user_passes_test(is_admin)
def create_table(request):
    if request.method == "POST":
        form = TableForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('menu:liste_table')
    else:
        form = TableForm()
    return render(request, "create_table.html", {'form': form})

# Fonction pour modifier une table, accessible uniquement aux administrateurs
@login_required
@user_passes_test(is_admin)
def edit_table(request, table_id):
    table = Table.objects.get(id=table_id)
    if request.method == "POST":
        form = TableForm(request.POST, instance=table)
        if form.is_valid():
            form.save()
            return redirect('menu:liste_table')
    else:
        form = TableForm(instance=table)
    return render(request, 'edit_table.html', {'form': form, 'table': table})

# Fonction pour supprimer une table, accessible uniquement aux administrateurs
@login_required
@user_passes_test(is_admin)
def delete_table(request, table_id):
    table = Table.objects.get(id=table_id)
    if request.method == "POST":
        table.delete()
        return redirect('menu:liste_table')
    return render(request, 'confirm_delete.html', {'table': table})

# Fonction pour afficher la liste des tables
def list_table(request):
    tables = Table.objects.all()
    return render(request, 'list_table.html', {'tables': tables})

@login_required
def service(request):
    return render(request, 'service.html')
