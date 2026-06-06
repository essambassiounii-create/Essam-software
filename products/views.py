from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def product_list(request):
    products = Product.objects.filter(is_active=True)
    categories = Category.objects.all()
    category_slug = request.GET.get('category')
    product_type = request.GET.get('type')

    if category_slug:
        products = products.filter(category__slug=category_slug)
    if product_type:
        products = products.filter(product_type=product_type)

    return render(request, 'products/product_list.html', {
        'products': products,
        'categories': categories,
        'selected_category': category_slug,
        'selected_type': product_type,
    })


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    related = Product.objects.filter(
        category=product.category, is_active=True
    ).exclude(pk=product.pk)[:3]
    return render(request, 'products/product_detail.html', {
        'product': product,
        'related': related,
    })
