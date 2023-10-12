from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.core import serializers
from main.forms import ProductForm
from django.urls import reverse
from main.models import Item
from django.db.models import Sum
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt 
import datetime
import json

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
    item.amount = max(1, item.amount - 1)
    item.save()
    return redirect('main:show_main')

def max(a, b):
    if a > b:
        return a
    return b

def get_product_json(request):
    product_item = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', product_item))

@csrf_exempt
def update_product_qty_ajax(request):
    if request.method == 'PUT':
        data = json.loads(request.body)
        product_id = data.get('character_id')
        product = Item.objects.get(pk=product_id)
        if data.get("modify") == "increment": 
            product.amount += 1
        if data.get("modify") == "decrement":
            product.amount = max(1, product.amount - 1)
        product.save()

        return HttpResponse(b"OK", status=200)

    return HttpResponseNotFound()

@csrf_exempt
def delete_product_ajax(request):
    if request.method == 'DELETE':
        product_id = json.loads(request.body).get('character_id')
        product = Item.objects.get(pk=product_id)
        product.delete()

        return HttpResponse(b"OK", status=200)

    return HttpResponseNotFound()

@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        rarity = request.POST.get("rarity")
        power = request.POST.get("power")
        description = request.POST.get("description")
        user = request.user

        new_product = Item(name=name, 
                           amount=amount, 
                           rarity=rarity,
                           power=power,
                           description=description, 
                           user=user)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()