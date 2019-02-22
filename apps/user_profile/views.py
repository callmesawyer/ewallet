from django.shortcuts import render, redirect

from django.views.generic import FormView
from django.views.generic import CreateView

from .models import Transaction, Profile, Account
from .forms import TransactionForm, CustomUserCreationForm

# def signup(request):
# 	template_name = "signup.html" 
# 	if request.method == 'POST':
# 		signup_form = CustomUserCreationForm(request.POST) # form with data
# 		if signup_form.is_valid():
# 			user = signup_form.save()

# 			profile = Profile.objects.create(user=user)
# 			account = Account.objects.create(user=user)
# 			profile.mobile = signup_form.cleaned_data['mobile']
# 			profile.save()
# 			account.save()

# 			return redirect('home')
# 	else:
# 		signup_form = CustomUserCreationForm() #unbounded form
# 	context = {
# 		'form': signup_form,
# 	}
# 	return render(request, template_name, context)

class SignUpView(CreateView):
	form_class = CustomUserCreationForm
	template_name = 'signup.html'
	success_url = '/'

	def form_valid(self, form):
		user = form.save()
		profile = Profile.objects.create(user=user)
		account = Account.objects.create(user=user)
		profile.mobile = form.cleaned_data['mobile']
		profile.save()
		account.save()
		return super().form_valid(form)



# class based view use is recommended by django
class TransactionView(CreateView):
	model = Transaction
	form_class = TransactionForm
	template_name = 'transaction.html'
	success_url = '/'


	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.from_user = self.request.user
		obj.save()
		return super().form_valid(form)