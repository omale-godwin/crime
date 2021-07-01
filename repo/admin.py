from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Report, Evident, Weakness

class ReportAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'regnumber', 'email', 'dats')
  list_display_links = ('id', 'name')
  search_fields = ('name', 'email', 'phone')
  list_per_page = 25

class WeaknessAdmin(admin.ModelAdmin):
  list_display = ('name', 'phone', 'dats')
  list_display_links = ('name',)
  search_fields = ('id',)
  list_per_page = 25

class EvidentAdmin(admin.ModelAdmin):
  list_display = ( 'id', 'photo_main', 'dates', 'user_id')
  list_display_links = ('photo_main' , 'id')
  search_fields = ('dats',)
  list_per_page = 25

admin.site.register(Report, ReportAdmin)
admin.site.register(Weakness, WeaknessAdmin)
admin.site.register(Evident, EvidentAdmin)
