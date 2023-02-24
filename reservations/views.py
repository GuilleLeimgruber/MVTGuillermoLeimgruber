from django.shortcuts import render

from django.http import HttpResponse

from django.views.generic import ListView, CreateView, DeleteView, UpdateView


import datetime

from reservations.models import Reservations

from reservations.forms import ReservationsForm


# Create your views here.

def create_reservation(request):

    if request.method == 'GET':
        context = {'form': ReservationsForm()}

        return render(request, 'reservations/create_reservation.html', context=context) 

    elif request.method == 'POST':

        form = ReservationsForm(request.POST)
        if form.is_valid():

            Reservations.objects.create(
                name = form.cleaned_data['name'], 
                dinner = form.cleaned_data['dinner'], 
                reservation_date = form.cleaned_data['reservation_date'],
            )
            context = {'message': 'Reserva creada'}
            return render(request, 'reservations/create_reservation.html', context=context)

        else:
                context = {
                    'form_errors': form.errors, 
                    'form': ReservationsForm()
                }
                return render(request, 'reservations/create_reservation.html', context=context)



def list_reservations(request):

    all_reservations = Reservations.objects.all()
    context = {'reservations': all_reservations}

    return render(request, 'reservations/list_reservations.html', context=context)



def update_reservation(request, pk):
    reservation = Reservations.objects.get(id=pk)

    if request.method == 'GET':

        context = {
            'form': ReservationsForm(
                initial={
                    'name': reservation.name,
                    'dinner': reservation.dinner,
                    'reservation_date': reservation.reservation_date,
                }
            )
        }
        
        return render(request, 'reservations/update_reservation.html', context=context)


    elif request.method == 'POST':

        form = ReservationsForm(request.POST)
        if form.is_valid():

            reservation.name = form.cleaned_data['name'] 
            reservation.dinner = form.cleaned_data['dinner'] 
            reservation.reservation_date = form.cleaned_data['reservation_date'] 
            reservation.save()
            
            context = {'message': 'Reservacion actualizada'}
            
        else:
                context = {
                    'form_errors': form.errors, 
                    'form': ReservationsForm()
                }
        return render(request, 'reservations/update_reservation.html', context=context)   





class ReservationsListView(ListView):

    model = Reservations
    template_name = 'reservations/list_reservations.html'
    success_url = '/reservations/list-reservations/'



class ReservationsCreateView(CreateView):

    model = Reservations
    template_name = 'reservations/create_reservation.html'
    fields = '__all__'
    success_url = '/reservations/list-reservations/'



class ReservationsUpdateView(UpdateView):

    model = Reservations
    template_name = 'reservations/update_reservation.html'
    fields = '__all__'
    success_url = '/reservations/list-reservations/'


class ReservationsDeleteView(DeleteView):

    model = Reservations
    template_name = 'reservations/delete_reservation.html'
    success_url = '/reservations/list-reservations/'

