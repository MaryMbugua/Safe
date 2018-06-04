from django.contrib import admin
from .models import Neighborhood,Business,Userm

# Register your models here.
admin.site.register(Neighborhood)
admin.site.register(Business)
admin.site.register(Userm)