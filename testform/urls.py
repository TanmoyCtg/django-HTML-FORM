from django.urls import path

from .views import homePage, successPage

urlpatterns = [
	path('', homePage, name='home'),
	path('success/', successPage, name='success'),
]