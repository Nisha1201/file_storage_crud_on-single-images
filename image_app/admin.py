from django.contrib import admin

# Register your models here.
from .models import Image

class imageAdmin(admin.ModelAdmin):
    list_display = ["id","title", "image_tag", "image"] # new

admin.site.register(Image, imageAdmin)