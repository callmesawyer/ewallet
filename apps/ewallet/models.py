from django.db import models

# Here models is a directory and Model is a class. Explore django > db > models in Github
class Profile(models.Model):
	MALE = 'm'
	FEMALE = 'f'
	GENDER_CHOICES = (
		(MALE, 'Male'),
		(FEMALE, 'Female')
	)
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
		return self.mobile_no