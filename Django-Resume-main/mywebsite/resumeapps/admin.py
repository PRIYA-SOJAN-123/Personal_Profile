from django.contrib import admin

# Register your models here.
from . models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'address', 'github')

# Register your models here.
admin.site.register(Profile, ProfileAdmin)