from django.contrib import admin
from datetime import date

from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	list_display = ('address', 'dob', 'mobile_no', 'country', 'gender', 'profession', 'get_age')
	list_display_links = ('address','mobile_no') # esma vako editable garna dinu mildaina
	list_editable = ('dob', 'country')
	list_filter = ('gender',)
	search_fields = ['address','mobile_no', 'country']

	def get_age(self, instance): # self ma ProfileAdmin ko instance aauxa, instance ma Profile ko instance aauxa
		age = date.today() - instance.dob
		return int(age.days//365.25)

	get_age.short_description = 'Age'
# admin.site.register(Profile, ProfileAdmin) # this is old way
