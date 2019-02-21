from django.contrib import admin
from datetime import date

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Profile, Transaction, Account


admin.site.unregister(User)

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class AccountInline(admin.StackedInline):
    model = Account
    can_delete = False
    verbose_name_plural = 'Account'
    fk_name = 'user'

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, AccountInline)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
	list_display = ('user', 'balance', 'point')


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
	list_display = ('from_user', 'to_user', 'amount', 'created_on')



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
