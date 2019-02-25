from django import forms
from django.contrib.auth.models import User

from .models import Transaction, Profile

from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class CustomUserCreationForm(UserCreationForm):
	mobile_no = forms.CharField(max_length=15)

	class Meta:
		model = User
		fields = ('username', 'email', 'mobile_no', 'first_name', 'last_name')

	def clean_email(self):
		email = self.cleaned_data.get('email')
		obj = User.objects.filter(email=email).exists()

		if obj:
			raise ValidationError(
				('Email already used: %(email)s'),
		    	params={'email': email},
				)
		return email.strip()

	def clean_mobile_no(self): # def clean(self) will validate all the fields of Profile, here clean_mobile_no will validate only mobile number
		mobile_no = self.cleaned_data.get('mobile_no') # get data from form
		obj = Profile.objects.filter(mobile_no=mobile_no).exists() # queryset, 

		# print(f'Cleaned mobile_no called {obj}')
		if obj:
			raise ValidationError(
		    ('Mobile number already used: %(mobile_no)s'),
		    params={'mobile_no': mobile_no},	
			)
		return mobile_no


class TransactionForm(forms.ModelForm):
	to_mobile = forms.CharField(max_length=15)

	class Meta:
		model = Transaction
		fields = ['to_mobile', 'amount']

# class TopUpForm(forms.ModelForm):
# 	amount = 
		