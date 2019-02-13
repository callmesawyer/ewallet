from django.contrib import admin

from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	list_display = ('address', 'dob', 'mobile_no', 'country', 'gender', 'profession')
	list_display_links = ('address','mobile_no') # esma vako editable garna dinu mildaina
	list_editable = ('dob', 'country')
	list_filter = ('gender',)
	search_fields = ['address','mobile_no', 'country']
# admin.site.register(Profile, ProfileAdmin) # this is old way
