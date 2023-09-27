from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.http import HttpResponseRedirect, HttpResponse
from django.core import serializers
from main.forms import ProductForm
from django.urls import reverse
from main.models import Item
from django.db.models import Sum
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    total_characters = Item.objects.filter(user=request.user).count() or 0
    total_pokemon = Item.objects.filter(user=request.user).aggregate(total_amount=Sum('amount'))['total_amount'] or 0
    items = Item.objects.filter(user=request.user)
    context = {
        'name':request.user.username,
        'class':'PBP-B',
        'char_name':'Pikachu',
        'char_description':'Pikachu, the most popular character.',
        'char_rarity':'Rare',
        'total_characters':total_characters,
        'total_pokemon':total_pokemon,
        'items':items,
        'last_login':request.COOKIES['last_login']
    }

    return render(request, 'main.html', context)

def create_item(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def delete_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    item.delete()
    return redirect('main:show_main')

def add_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    item.amount += 1
    item.save()
    return redirect('main:show_main')

def subtract_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    item.amount = max(0, item.amount - 1)
    item.save()
    return redirect('main:show_main')

def max(a, b):
    if a > b:
        return a
    return b