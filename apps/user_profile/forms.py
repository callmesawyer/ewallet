from django import forms
from django.contrib.auth.models import User

from .models import Transaction

from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
	mobile = forms.CharField(max_length=15)

	class Meta:
		model = User
		fields = ('username', 'email', 'mobile')

class TransactionForm(forms.ModelForm):

	class Meta:
		model = Transaction
		fields = ['to_user', 'amount']
		