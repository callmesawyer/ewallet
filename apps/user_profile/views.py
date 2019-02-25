from django.shortcuts import render, redirect

from django.views.generic import FormView
from django.views.generic import CreateView, DetailView, UpdateView

from .models import Transaction, Profile, Account
from .forms import TransactionForm, CustomUserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError


class SignUpView(CreateView):
	form_class = CustomUserCreationForm
	template_name = 'signup.html'
	success_url = '/'

	def form_valid(self, form):
		user = form.save()
		mobile_no = form.cleaned_data.get('mobile_no')
		# print(f'Form Validate {mobile_no}')
		Profile.objects.create(user=user, mobile_no=mobile_no) # mobile_field_name = mobie
		Account.objects.create(user=user, balance=50, point=10)
		
		return super().form_valid(form)



# class based view use is recommended by django
class TransactionView(CreateView):
	model = Transaction
	form_class = TransactionForm
	template_name = 'transaction.html'
	success_url = '/'
 

	def form_valid(self, form):
		to_mobile = form.cleaned_data.get('to_mobile')
		if self.request.user.profile.mobile_no == to_mobile:
			raise ValidationError('Balance cant transfer to itself')
		obj = form.save(commit=False)
		obj.from_user = self.request.user
		obj.to_user = Profile.objects.get(mobile_no=to_mobile).user
		obj.save()
		return super().form_valid(form)

class UserDetailView(LoginRequiredMixin, DetailView):
	model = User
	template_name = 'user_detail.html'

	def get_object(self, queryset=None):
		if queryset is None:
			queryset = self.get_queryset()
		if self.request.user.id:
			queryset = queryset.filter(pk=self.request.user.id) # filter logged in user
			obj = queryset.get()
			return obj


# class AccountUpdateView(UpdateView):
# 	model = 

