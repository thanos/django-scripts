from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify
from fields import PythonCodeField




class Script(models.Model):
	name = models.CharField(_('name'), max_length = 100)
	slug = models.SlugField(_('slug'), max_length=100)
	description = models.TextField(_('description'),)
	source = PythonCodeField(blank=True, null=True)
	
	def __unicode__(self):
         return self.name

   