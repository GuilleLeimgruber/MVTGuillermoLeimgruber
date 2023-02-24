from django.shortcuts import render

from django.http import HttpResponse



from django.views.generic import ListView, CreateView, DeleteView, UpdateView


from deliveries.models import Deliveries

from deliveries.forms import DeliveryForm

# Create your views here.


def create_delivery(request):
    if request.method == 'GET':
        context = {
            'form': DeliveryForm()
        }
        
        return render(request, 'deliveries/create_delivery.html', context=context)


    elif request.method == 'POST':
        form = DeliveryForm(request.POST)
        if form.is_valid():

            Deliveries.objects.create(
                client = form.cleaned_data['client'], 
                menu = form.cleaned_data['menu'], 
                payment_method = form.cleaned_data['payment_method'],
            )
            context = {
                'message': 'Delivery creado'
            }
            return render(request, 'deliveries/create_delivery.html', context=context)

        else:
            context = {
                'form_errors': form.errors, 
                'form': DeliveryForm()
            }
            return render(request, 'deliveries/create_delivery.html', context=context)
      


def list_deliveries(request):
    deliveries = Deliveries.objects.all()
    context = {
        'deliveries': deliveries

    }

    return render(request, 'deliveries/list_deliveries.html', context = context)



def update_delivery(request, pk):
    delivery = Deliveries.objects.get(id=pk)

    if request.method == 'GET':
        
        context = {
            'form': DeliveryForm(
                initial={
                    'client': delivery.client, 
                    'menu': delivery.menu,
                    'payment_method': delivery.payment_method,
                }
            )
        }
        
        return render(request, 'deliveries/update_delivery.html', context=context)


    elif request.method == 'POST':

        form = DeliveryForm(request.POST)
        if form.is_valid():

            delivery.client = form.cleaned_data['client'] 
            delivery.menu = form.cleaned_data['menu'] 
            delivery.payment_method = form.cleaned_data['payment_method']
            delivery.save()
            
            context = {'message': 'Delivery actualizado'}
          
        else:
                context = {
                    'form_errors': form.errors, 
                    'form': DeliveryForm()
                }
        return render(request, 'deliveries/update_delivery.html', context=context)














class DeliveriesCreateView(CreateView):

    model = Deliveries
    template_name = 'deliveries/create_delivery.html'
    fields = '__all__'
    success_url = '/deliveries/list-deliveries/'


class DeliveriesListView(ListView):

    model = Deliveries
    template_name = 'deliveries/list_deliveries.html'
    success_url = '/deliveries/list-deliveries/'

class DeliveriesUpdateView(UpdateView):

    model = Deliveries
    template_name = 'deliveries/update_delivery.html'
    fields = '__all__'
    success_url = '/deliveries/list-deliveries/'


class DeliveriesDeleteView(DeleteView):

    model = Deliveries
    template_name = 'deliveries/delete_delivery.html'
    success_url = '/deliveries/list-deliveries/'


