from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
	fields = ['intra_id', 'intra_username', 'first_name', 'last_name', 'email', 'bio'] #edit and create
	list_display = ('updated_at', 'intra_username', 'first_name', 'last_name', 'email', 'bio') #showing 

admin.site.register(User, UserAdmin)