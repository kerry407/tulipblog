from django.contrib import admin
from .models import Profile
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id','user','first_name','last_name','city', 'bio']

admin.site.register(Profile,ProfileAdmin)
