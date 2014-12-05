from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify
from fields import PythonCodeField




class Script(models.Model):
	name = models.CharField(_('name'), max_length = 100, unique=true)
	slug = models.SlugField(_('slug'), max_length=100)
	description = models.TextField(_('description'),)
	created_by models.CharField(_('created  by'), max_length = 100)
	created_on = models.DateTimeField(_('updated by'), auto_now_add=True)

	def __unicode__(self):
        return self.name

	def save(self, **kwargs):
		if not self.id:
    		self.slug = slugify(self, self.name) 
    	super(Script, self).save(**kwargs)

class Version(models.Model):
	class Meta:
		unique_together = ("driver", "restaurant")
		order_with_respect_to = 'script'
		ordering = ['name', '-version']
	script = models.ForeignKey(Script)	
    version = models.PositiveSmallIntegerField(_('version'), default=1)
    comment = models.TextField(_('comment'), blank=True)
    source = PythonCodeField(_('source'), blank=True, null=True)
    updated_on = models.DateTimeField(_('updated on'), auto_now=True, auto_now_add=True)
    updated_by = models.CharField(_('updated by'), max_length = 100))
     

	def save(self, **kwargs):
    	self.version = self.objects.count()+1
    	super(Version, self).save(**kwargs)

    def __unicode__(self):
        return self.name+'-'+self.version