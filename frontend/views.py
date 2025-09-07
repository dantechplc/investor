from django.shortcuts import render

# Create your views here.

def HomeView(request):
    context = {
        'navbar':'home'
    }
    return render(request, 'frontend/home.html', context)


def MarketView(request):
    context = {
        'navbar':'markets'
    }
    return render(request, 'frontend/market.html', context)


def AboutView(request):
    context = {
        'navbar':'about'
    }
    return render(request, 'frontend/about.html', context)

def ContactView(request):
    context = {
        'navbar':'contact'
    }
    return render(request, 'frontend/contact.html', context)

def CustomerView(request):
    context = {
        'navbar':'customer'
    }
    return render(request, 'frontend/customer.html', context)

def LegalView(request):
    context = {
        'navbar':'legal'
    }
    return render(request, 'frontend/legal.html', context)