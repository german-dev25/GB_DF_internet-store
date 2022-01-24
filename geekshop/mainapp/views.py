from django.shortcuts import render
import json

MENU_LINKS = [
    {'url': 'main', 'name': 'домой'},
    {'url': 'products', 'name': 'продукты'},
    {'url': 'contact', 'name': 'контакты'},
]

# PRODUCTS_CATEGORY = ['все', 'дом', 'офис', 'модерн', 'классика', ]
# PRODUCTS_CATEGORY_HREF = ['#', '#', '#', '#', '#', ]

PRODUCTS_LINKS = [
    {'href': '#', 'name': 'все'},
    {'href': '#', 'name': 'дом'},
    {'href': '#', 'name': 'офис'},
    {'href': '#', 'name': 'модерн'},
    {'href': '#', 'name': 'классика'},
]

def index(request):
    return render(request, 'mainapp/index.html', context={
        'title': 'Главная',
        'menu_links': MENU_LINKS,
    })


def products(request):
    with open('products.json', 'r', encoding='UTF-8') as file:
        products = json.load(file)

    return render(request, 'mainapp/products.html', context={
        'title': 'Продукты',
        'menu_links': MENU_LINKS,
        'products': products,
        'products_menu': PRODUCTS_LINKS,
    })


def contact(request):
    return render(request, 'mainapp/contact.html', context={
        'title': 'Контакты',
        'menu_links': MENU_LINKS,
    })
