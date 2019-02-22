from django.urls import path

from django.contrib.auth.views import LoginView

from .views import TransactionView, SignUpView

urlpatterns = [
	path('signup/', SignUpView.as_view(), name='signup'),
	path('send/', TransactionView.as_view(), name="send"),
	path('login/', LoginView.as_view(template_name='login.html'), name='login'), # class based views ma as_view() method call garnu parxas
]