import stripe
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from basket.basket import Basket


@login_required
def BasketView(request):
    basket = Basket(request)
    total = str(basket.get_total_price())
    total = total.replace('.', '')
    total = int(total)

    stripe.api_key = 'sk_test_51HX5u6A1fnSIB3Kmi9YWFTtgVrcE0bOv5zNYToTO4aAqCY4aYD6LPAhAwxvyGC7LIxYG5S402ylsKkrjWnonqmCH00Oq6E6YtR'
    intent = stripe.PaymentIntent.create(
        amount=total,
        currency='gbp',
        metadata={'userid': request.user.id}
    )

    return render(request, 'payment/payment_home.html', {'client_secret': intent.client_secret})
