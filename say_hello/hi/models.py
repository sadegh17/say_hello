from django.db import models
from django.db.models.signals import pre_save
from .validation import email_valid

# Create your models here. 
class FaveRest(models.Model):
	name = models.CharField(max_length=120)
	locat = models.CharField(max_length=120 , null=True)
	email  = models.EmailField(max_length=254,null=True ,blank = True , validators= [email_valid])
	addTime = models.TimeField( auto_now_add=True )
	upTime = models.TimeField( auto_now=True )
	slug = models.SlugField(null=True,blank=True)

	category_CHOICES = (
		('soup',(( 'onso' , 'oniensoup'),('joso','soupjo'))),
		('pizza', (('makhp','makhsus'),('peppi','peperoni'))),
		('sand', 'sandwich'),
		('drink', 'drink')
	)
	category = models.CharField(
	max_length=5,
	choices=category_CHOICES,
	default='drink',
	)

	def __str__(self):
		return self.name

def fr_pre_save_rec(sender , instance,*args,**kwargs):
	if not instance.slug:
		instance.slug = instance.name

pre_save.connect(fr_pre_save_rec , sender=FaveRest)