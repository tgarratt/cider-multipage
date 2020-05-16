from django.contrib import admin
from .models import add_bottle, add_crate, add_keg

admin.site.register(add_bottle)

admin.site.register(add_crate)

admin.site.register(add_keg)