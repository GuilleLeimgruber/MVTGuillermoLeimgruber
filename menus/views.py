from re import search


from django.shortcuts import render

from django.http import HttpResponse

from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from menus.models import Menus, Categories

from menus.forms import MenuForm

# Create your views here.







def create_menu(request):

    if request.method == 'GET':

        context = {'form': MenuForm()}
        
        return render(request, 'menus/create_menu.html', context=context)


    elif request.method == 'POST':

        form = MenuForm(request.POST)
        if form.is_valid():

            Menus.objects.create(
                name = form.cleaned_data['name'], 
                price = form.cleaned_data['price'], 
                stock = form.cleaned_data['stock'],
            )
            context = {'message': 'Menu creado'}
            return render(request, 'menus/create_menu.html', context=context)

        else:
                context = {
                    'form_errors': form.errors, 
                    'form': MenuForm()
                }
                return render(request, 'menus/create_menu.html', context=context)
      


def list_menus(request):

    if 'search' in request.GET:
        search = request.GET['search']

        menus = Menus.objects.filter(name__contains=search)
    
    else:

        menus = Menus.objects.all()
    context = {'menus': menus}

    return render(request, 'menus/list_menus.html', context=context)



def update_menu(request, pk):
    menu = Menus.objects.get(id=pk)

    if request.method == 'GET':

        context = {
            'form': MenuForm(
                initial={
                    'name': menu.name, 
                    'price': menu.price, 
                    'sotck': menu.stock,
                }
            )
        }
        
        return render(request, 'menus/update_menu.html', context=context)


    elif request.method == 'POST':

        form = MenuForm(request.POST)
        if form.is_valid():

            menu.name = form.cleaned_data['name'], 
            menu.price = form.cleaned_data['price'], 
            menu.stock = form.cleaned_data['stock'], 
            menu.save()
            
            context = {'message': 'Menu actualizado'}
            
        else:
                context = {
                    'form_errors': form.errors, 
                    'form': MenuForm()
                }
        return render(request, 'menus/update_menu.html', context=context)
      


def create_category(request):

    return HttpResponse('Se creo una nueva categoria')



def list_categories(request):

    all_categories = Categories.objects.all()
    context = {'categories': all_categories}

    return render(request, 'categories/list_categories.html', context=context)   













class MenusCreateView(CreateView):

    model = Menus
    template_name = 'menus/create_menu.html'
    fields = '__all__'
    success_url = '/menus/list-menus/'




class MenusUpdateView(UpdateView):

    model = Menus
    template_name = 'menus/update_menu.html'
    fields = '__all__'
    success_url = '/menus/list-menus/'



class MenusDeleteView(DeleteView):

    model = Menus
    template_name = 'menus/delete_menu.html'
    success_url = '/menus/list-menus/'
