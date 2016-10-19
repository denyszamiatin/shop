from django.contrib import admin
from .models import Cpu, Good, Tag, Image

class GoodAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Cpu)
admin.site.register(Good, GoodAdmin)
admin.site.register(Tag)
admin.site.register(Image)

#qwerty123