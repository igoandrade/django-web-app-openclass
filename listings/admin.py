from django.contrib import admin
from listings.models import Band

class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_formed', 'genre')

# Register your models here.
admin.site.register(Band, BandAdmin)
