from django.shortcuts import render
from products.models import Product, Category
from core.models import Service


def home(request):
    latest_products = Product.objects.filter(is_active=True).order_by('-created_at')[:6]
    services = Service.objects.filter(is_active=True)[:4]
    stats = {
        'products_count': Product.objects.filter(is_active=True).count(),
        'clients_count': 150,
        'projects_count': 200,
        'years_count': 5,
    }
    return render(request, 'core/home.html', {
        'latest_products': latest_products,
        'services': services,
        'stats': stats,
    })


def about(request):
    return render(request, 'core/about.html')


def services(request):
    all_services = Service.objects.filter(is_active=True)
    return render(request, 'core/services.html', {'services': all_services})
