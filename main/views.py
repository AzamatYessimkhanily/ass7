from django.shortcuts import render
from .models import Clothing,Shoes,Аccessories
from .forms import ClothingFilterForm,ShoesFilterForm,AccessFilterForm
from django.db.models import Q
def index(request):
    return render(request, 'index.html')
def clothing(request):
    clothing_list = Clothing.objects.all()
    filter_form = ClothingFilterForm(request.GET)
    if filter_form.is_valid():
        clothing_type = filter_form.cleaned_data['clothing_type']
        size = filter_form.cleaned_data['size']
        color = filter_form.cleaned_data['color']
        min_price = filter_form.cleaned_data['min_price']
        max_price = filter_form.cleaned_data['max_price']
        if clothing_type:
            clothing_list = clothing_list.filter(name__in=clothing_type)
        if size:
            # create a list of all sizes selected by the user
            selected_sizes = list(size)
            # create an empty Q object
            q = Q()
            # add a filter to the Q object for each selected size
            for selected_size in selected_sizes:
                q |= Q(size__contains=selected_size)
            # filter the clothing by the Q object
            clothing_list = clothing_list.filter(q)
        if color:
            clothing_list = clothing_list.filter(color__in=color)
        if min_price:
            clothing_list = clothing_list.filter(price__gte=min_price)
        if max_price:
            clothing_list = clothing_list.filter(price__lte=max_price)
    return render(request, 'clothing.html', {'clothing_list': clothing_list, 'filter_form': filter_form})
def shoes(request):
    shoes_list = Shoes.objects.all()
    filter_form = ShoesFilterForm(request.GET)
    if filter_form.is_valid():
        shoe = filter_form.cleaned_data['shoe_type']
        size = filter_form.cleaned_data['size']
        color = filter_form.cleaned_data['color']
        min_price = filter_form.cleaned_data['min_price']
        max_price = filter_form.cleaned_data['max_price']
        if shoe:
            shoes_list = shoes_list.filter(name__in=shoe)
        if size:
            # create a list of all sizes selected by the user
            selected_sizes = list(size)
            # create an empty Q object
            q = Q()
            # add a filter to the Q object for each selected size
            for selected_size in selected_sizes:
                q |= Q(size__contains=selected_size)
            # filter the clothing by the Q object
            shoes_list = shoes_list.filter(q)
        if color:
            shoes_list = shoes_list.filter(color__in=color)
        if min_price:
            shoes_list= shoes_list.filter(price__gte=min_price)
        if max_price:
            shoes_list = shoes_list.filter(price__lte=max_price)
    return render(request, 'shoes.html', {'shoes_list': shoes_list,'filter_form': filter_form})
def access(request):
    access_list = Аccessories.objects.all()
    filter_form = AccessFilterForm(request.GET)
    if filter_form.is_valid():
        access = filter_form.cleaned_data['access_type']
        color = filter_form.cleaned_data['color']
        min_price = filter_form.cleaned_data['min_price']
        max_price = filter_form.cleaned_data['max_price']
        if access:
            access_list = access_list.filter(name__in=access)
        if color:
            access_list = access_list.filter(color__in=color)
        if min_price:
            access_list= access_list.filter(price__gte=min_price)
        if max_price:
            access_list = access_list.filter(price__lte=max_price)
    return render(request, 'access.html', {'access_list': access_list,'filter_form': filter_form})
def about(request):
    return render(request, 'О-нас.html')



