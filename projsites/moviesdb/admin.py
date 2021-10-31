from django.contrib import admin

# Register your models here.
from .models import Movie, Grade

admin.site.register(Movie)
admin.site.register(Grade)