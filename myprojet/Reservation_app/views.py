from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from myapp.models import Reservation 

from .forms import ReservationForm
from django.contrib import messages


@login_required
def reservation_view(request):
    """View pou kreye yon nouvo rezèvasyon."""
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.utilisateur = request.user  # Mete itilizatè ki soumèt la
            reservation.save()
            form.save_m2m()  # Pou ManyToManyField yo
            return redirect('liste_reservation')
    else:
        form = ReservationForm()

    return render(request, 'creer_reservations.html', {'form': form})

@login_required
def reservation_list(request):
    """View pou montre lis rezèvasyon yo pou itilizatè ki konekte a."""
    reservations = Reservation.objects.all()
    return render(request, 'liste_reservation.html', {'reservations': reservations})




 

def is_admin(user):
    """Verifier sur un admin."""
    return user.is_superuser

@login_required
def update_reservation(request, reservation_id):
    """View pou modifye yon rezèvasyon."""
    reservation = get_object_or_404(Reservation, id=reservation_id)

    # Se sèlman moun ki kreye rezèvasyon an oswa admin ki ka modifye li
    if request.user != reservation.utilisateur and not request.user.is_superuser:
        messages.error(request, "Ou pa gen otorizasyon pou modifye rezèvasyon sa.")
        return redirect('reservation_list')

    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            messages.success(request, "Rezèvasyon an modifye ak siksè!")
            return redirect('liste_reservation')
    else:
        form = ReservationForm(instance=reservation)

    return render(request, 'reservation_update.html', {'form': form, 'reservation': reservation})




@login_required
def delete_reservation(request, reservation_id):
    """View pou efase yon rezèvasyon."""
    reservation = get_object_or_404(Reservation, id=reservation_id)

    
    if request.user != reservation.utilisateur and not request.user.is_superuser:
        messages.error(request, "Ou pa gen otorizasyon pou efase rezèvasyon sa.")
        return redirect('liste_reservation')

    if request.method == 'POST':
        reservation.delete()
        messages.success(request, "Reservations suprimer avec success!")
        return redirect('liste_reservation')

    return render(request, 'reservation_confirm_delete.html', {'reservation': reservation})
