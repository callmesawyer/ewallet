from django.contrib import admin
from datetime import date

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Profile


admin.site.unregister(User)

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)





# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
# 	list_display = ('address', 'dob', 'mobile_no', 'country', 'gender', 'profession', 'get_age')
# 	list_display_links = ('address','mobile_no') # esma vako editable garna dinu mildaina
# 	list_editable = ('dob', 'country')
# 	list_filter = ('gender',)
# 	search_fields = ['address','mobile_no', 'country']

# 	def get_age(self, instance): # self ma ProfileAdmin ko instance aauxa, instance ma Profile ko instance aauxa
# 		age = date.today() - instance.dob
# 		return int(age.days//365.25)

# 	get_age.short_description = 'Age'
# # admin.site.register(Profile, ProfileAdmin) # this is old way
