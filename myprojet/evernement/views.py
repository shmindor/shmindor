from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from myapp.models import Evenement
from .forms import EvenementForm
from django.utils.timezone import now


# Vérifier si l'utilisateur est admin
def est_admin(user):
    return user.is_staff   
# Liste des événements
def liste_evenements(request):
    evenements = Evenement.objects.filter(date__gte=now().date())  # Se sèlman evènman k ap vini yo
    return render(request, 'liste_evernement.html', {'evenements': evenements})

# Détail d'un événement
def detail_evenement(request, evenement_id):
    evenement = get_object_or_404(Evenement, id=evenement_id)
    return render(request, 'detail.html', {'evenement': evenement})

# Ajouter un événement (admin seulement)
@login_required
@user_passes_test(est_admin)
def ajouter_evenement(request):
    if request.method == "POST":
        form = EvenementForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('liste_evenements')
    else:
        form = EvenementForm()
    return render(request, 'ajouter_evenement.html', {'form': form, 'titre': 'Ajouter un événement'})

# Modifier un événement (admin seulement)
@login_required
@user_passes_test(est_admin)
def modifier_evenement(request, evenement_id):
    evenement = get_object_or_404(Evenement, id=evenement_id)
    if request.method == "POST":
        form = EvenementForm(request.POST, instance=evenement)
        if form.is_valid():
            form.save()
            return redirect('liste_evenements')
    else:
        form = EvenementForm(instance=evenement)
    return render(request, 'update_evernement.html', {'form': form, 'titre': 'Modifier l\'événement'})

# Supprimer un événement (admin seulement)
@login_required
@user_passes_test(est_admin)
def supprimer_evenement(request, evenement_id):
    evenement = get_object_or_404(Evenement, id=evenement_id)
    if request.method == "POST":
        evenement.delete()
        return redirect('liste_evenements')
    return render(request, 'confirmer_suppression.html', {'evenement': evenement})
