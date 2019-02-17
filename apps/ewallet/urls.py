from django.urls import path

from .views import home, contact

urlpatterns = [
	path('', home, name='home'),  # template bata call garda name use garinxa
    path('contact/', contact, name='contact'),
]