from django.contrib import admin

# Register your models here.
from .models import studiocoaches

class studiocoachesAdmin(admin.ModelAdmin):
    list_display=['esm', 'id', 'famil', 'tarikhtavalod', 'roozayekelas','saatekelas', 'income_per_hours']

admin.site.register(studiocoaches, studiocoachesAdmin)
