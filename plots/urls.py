from django.urls import path
from .views import index, logout_view, products

urlpatterns = [
	path('', index, name='index'),
	path('logout', logout_view, name='logout'),
	path('products', products, name='products'),
]