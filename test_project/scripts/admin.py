from django.contrib import admin

# Register your models here.
class Script(models.Model):
	name = models.CharField(_('name'), max_length = 100)
	slug = models.SlugField(_('slug'), max_length=100)
	description = models.TextField(_('description'),)
	created_by models.CharField(_('created  by'), max_length = 100)
	created_on = models.DateTimeField(_('created_on'), auto_now_add=True)

class Version(models.Model):
	head = models.BooleanField(default=True)
    version = models.PositiveSmallIntegerField(_('version'), default=1)
    comment = models.TextField(_('comment'), blank=True)
    source = PythonCodeField(_('source'), blank=True, null=True)
    updated_on = models.DateTimeField(_('updated on'), auto_now=True, auto_now_add=True)
    updated_by = models.CharField(_('updated by'), max_length = 100))
    script = models.ForeignKey(Script) 








from django.contrib import admin
from models import Script
class ScriptAdmin(admin.AdminModel):
    date_hierarchy = 'created_on'
    list_display = ['name', 'slug', 'created_by', 'created_on', 'description']
    list_filter = ['enabled', ]
    search_fields = ['name', 'description']
    prepopulated_fields = {"slug": ("name",)}



admin.site.register(Source, SourceAdmin)