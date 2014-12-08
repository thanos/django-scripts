from django.contrib import admin
import reversion



from django.contrib import admin
from models import Script
class ScriptAdmin(reversion.VersionAdmin):
    list_display = ['name', 'slug',  'description']
    search_fields = ['name', 'description', 'source']
    prepopulated_fields = {"slug": ("name",)}



admin.site.register(Script, ScriptAdmin)