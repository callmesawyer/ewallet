from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
	MALE = 'm'
	FEMALE = 'f'
	GENDER_CHOICES = (
		(MALE, 'Male'),
		(FEMALE, 'Female')
	)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	profile_pic = models.ImageField(upload_to='profile', null=True, blank=True)
	address = models.CharField(max_length=30)
	country = models.CharField(max_length=30)
	mobile_no = models.CharField(max_length=15, unique=True)
	dob = models.DateField()
	gender = models.CharField(max_length=6,
						choices=GENDER_CHOICES)
	profession = models.CharField(max_length=20)

	def save(self, *args, **kwargs): # override save method
		self.address = self.address.capitalize()
		super().save(*args, **kwargs)

	def __str__(self):
		return self.user.username

class Account(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	balance = models.DecimalField(max_digits=5, decimal_places=2)
	point = models.DecimalField(max_digits=5, decimal_places=2)

class Transaction(models.Model):
	from_user = models.ForeignKey(User, related_name='from_user',on_delete=models.CASCADE)
	to_user = models.ForeignKey(User, related_name='to_user', on_delete=models.SET_NULL, null=True)
	amount = models.DecimalField(max_digits=4, decimal_places=2)
	created_on = models.DateTimeField('transaction_time', auto_now_add=True)

	def __str__(self):
		return 'From: {} to {} Amount {}'.format(self.from_user, self.to_user, self.amount)


@receiver(post_save, sender=Transaction)
def transfer_balance(sender, instance, created, **kwargs):
	if created:
		from_user = User.objects.get(pk=instance.from_user.pk).account
		to_user = User.objects.get(pk=instance.to_user.pk).account

		from_user.balance -= instance.amount
		to_user.balance += instance.amount
		from_user.save()
		to_user.save()