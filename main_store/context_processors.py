from .models import Category, Product



def categories(request):
    return {
        'categories': Category.objects.filter(level=0)
    }

def products(request):
    return {
        'products': Product.objects.all(),

    }
