from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There is nothing in your bag at the moment")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Msh7dJ2VFYKktILN05RkyiL74k3GCg7h2aqaXn6j20je9Yi8iCmE3rigoTLFy3jcus8LIpQA7CpnSWgid4KzsP100fYcsTmki',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)