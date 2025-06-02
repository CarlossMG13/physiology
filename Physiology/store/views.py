# store/views.py
# store/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')

def shop(request):
    return render(request, 'store/shop.html')  
    
def skin_guide(request):
    return render(request, 'store/skin_guide.html')  

def the_brand(request):
    return render(request, 'store/the_brand.html')  

def the_journaling(request):
    return render(request, 'store/the_journaling.html')  

def contact(request):
    return render(request, 'store/contact.html')  

def faq(request):
    return render(request, 'store/faq.html')  

def shipping(request):
    return render(request, 'store/shipping.html')  

def returns(request):
    return render(request, 'store/returns.html')  

def terms(request):
    return render(request, 'store/terms.html')  

def privacy_policy(request):
    return render(request, 'store/privacy_policy.html')  

def partners(request):
    return render(request, 'store/partners.html')  

def find_distributor(request):
    return render(request, 'store/find_distributor.html')  

def become_distributor(request):
    return render(request, 'store/become_distributor.html')  

def benefits(request):
    return render(request, 'store/benefits.html')  

def distribution_info(request):
    return render(request, 'store/distribution_info.html')  

def minimalist_philosophy(request):
    return render(request, 'store/minimalist_philosophy.html')  

def radiant_skin(request):
    return render(request, 'store/radiant_skin.html')  

def essential_only(request):
    return render(request, 'store/essential_only.html')  

def minimalist_philosophy_2(request):
    return render(request, 'store/minimalist_philosophy_2.html')  

