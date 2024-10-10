from django.http import JsonResponse
from .models import Category, Product

def category_list(request):
    categories = Category.objects.all()
    data = []

    for category in categories:
        data.append({
            'id': category.id,
            'name': category.name,
            'parent id': category.parent.id if category.parent else None,
            'parent name': category.parent.name if category.parent else None,
        })
    return JsonResponse(data, safe=False)


def product_list(request):
    products = Product.objects.all()
    data = {}

    for product in products:
        data[f'product {product.id}'] = {
            'name': product.name,
            'price': product.price,
            'quantity': product.quantity,
            'image': product.image.url if product.image else None,
            'category': [{
                'category id': category.id,
                'category name': category.name
            } for category in product.categories.all()
            ]
        }
    return JsonResponse(data, safe=False)
