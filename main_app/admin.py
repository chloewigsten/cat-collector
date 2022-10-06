from django.contrib import admin
from .models import Breed, Characteristics, Color, Personality

# Register your models here.
admin.site.register(Breed)
admin.site.register(Color)
admin.site.register(Characteristics)
admin.site.register(Personality)