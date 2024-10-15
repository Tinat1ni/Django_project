from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.db.models import Count
from django.db.models import Max, Min, Avg, F
#from django.core.paginator import Paginator


def category_list(request):
    top_level_categories = (Category.objects.filter(parent__isnull=True)
    .prefetch_related('products', 'children__products')
    .annotate(products_in_category=Count('products', distinct=True)
                                  +Count('children__products', distinct=True)
       )
    )
    context = {
        'top_level_categories': top_level_categories,
    }
    return render(request, 'category_list.html', context)


def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)

    products = category.products.prefetch_related('categories')
    subcategory_products = Product.objects.filter(categories__in=category.children.all())

    combined_products = products | subcategory_products
    combined_products = combined_products.annotate(total_value=F('price') * F('quantity'))

    cheapest = combined_products.aggregate(Min('price'))['price__min'] or 0
    most_expensive = combined_products.aggregate(Max('price'))['price__max'] or 0
    average_price = combined_products.aggregate(Avg('price'))['price__avg'] or 0
    total_value = sum(product.price * product.quantity for product in combined_products) or 0

    context = {
        'category': category,
        'products': combined_products,
        'cheapest': cheapest,
        'most_expensive': most_expensive,
        'average_price': average_price,
        'total_value': total_value,
    }

    return render(request, 'category_products.html', context)


def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    image_url = product.image.url if product.image else None
    context = {
        'product': product,
        'image_url': image_url
    }

    return render(request, 'product_details.html', context)


