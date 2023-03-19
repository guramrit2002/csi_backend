from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Sig)
admin.site.register(Team)
admin.site.register(Event)
admin.site.site_header = 'CSI Admin Panel'
# admin.site.register(Master)