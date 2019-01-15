from django.contrib import admin

# Register your models here.
from SkateApp.models import Image, UserProfile

admin.site.register(Image)
admin.site.register(UserProfile)
