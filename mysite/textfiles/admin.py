from django.contrib import admin

# Register your models here.
from .models import TextFile, Image, Group

admin.site.register(TextFile)
admin.site.register(Image)
admin.site.register(Group)
