"""
URL configuration for Physiology project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# physiology/physiology/Physiology/urls.py
from django.contrib import admin
from django.urls import path
from store import views  # Importa tus vistas desde la aplicación 'store'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),  # La página de inicio
    path('shop/', views.shop, name='shop'),
    path('skin-guide/', views.skin_guide, name='skin_guide'),
    path('the-brand/', views.the_brand, name='the_brand'),
    path('the-journaling/', views.the_journaling, name='the_journaling'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('shipping/', views.shipping, name='shipping'),
    path('returns/', views.returns, name='returns'),
    path('terms/', views.terms, name='terms'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('partners/', views.partners, name='partners'),
    path('find-distributor/', views.find_distributor, name='find_distributor'),
    path('become-distributor/', views.become_distributor, name='become_distributor'),
    path('benefits/', views.benefits, name='benefits'),
    path('distribution-info/', views.distribution_info, name='distribution_info'),
    path('minimalist-philosophy/', views.minimalist_philosophy, name='minimalist_philosophy'),
    path('radiant-skin/', views.radiant_skin, name='radiant_skin'),
    path('essential-only/', views.essential_only, name='essential_only'),
    path('minimalist-philosophy-2/', views.minimalist_philosophy_2, name='minimalist_philosophy_2'),
]