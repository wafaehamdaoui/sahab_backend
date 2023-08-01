from django.contrib import admin
from .models import Counter, Report, Image
# Register your models here.
admin.site.register(Counter)
admin.site.register(Image)
admin.site.register(Report)
