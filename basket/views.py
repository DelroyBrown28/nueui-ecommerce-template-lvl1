from django.shortcuts import render


def basket_summary(request):
    return render(request, 'main_store/basket/summary.html')
