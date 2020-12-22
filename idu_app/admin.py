from django.contrib import admin
from idu_app import models

# Register your models here.
admin.site.register(models.student)
admin.site.register(models.mark)
admin.site.register(models.contact)