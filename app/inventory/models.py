from django.db import models

#Pull in central model from each of the following apps
from organizations.models import Organization
from people.models import Person
from places.models import Location
from django.contrib.auth.models import User

#User editable list of TGM Genres
#For definition of Genres in the TGM see https://www.loc.gov/rr/print/tgm2/
class TGM_Genre(models.Model):
	name = models.CharField(max_length=50)
	notes = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.name

#User editable list of all previous inventories/other sources of data for the inventory
class Original_Source(models.Model):
	name = models.CharField(max_length=765)
	notes = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.name

#Fields pulled almost verbatim from most recent inventory, which was designed by Alexandra Montgomery
#Heavily based on MARC format
class Item(models.Model):
	#Choice lists used in fields below
	DATE_CERTAINTY_CHOICES = [
		(0, "undated"),
		(1, "cannot be verified"),
		(2, "uncertain"),
		(3, "possible"),
		(4, "likely"),
		(5, "verified")
	]
	DIGITIZATION_CHOICES = [
		('yes', 'yes'),
		('no', 'no'),
		('maybe', 'maybe')
	]
	RECORD_STATUS_CHOICES = [
		('complete', 'complete'),
		('incomplete', 'incomplete'),
		('review', 'review'),
		('reviewed', 'reviewed')
	]
	IONA_HOLDINGS_CHOICES = [
		('original', 'original'), 
		('copy', 'copy'),
		('original_copy', 'original and copy')
	]

	accession_number = models.CharField(max_length=100, blank=True, null=True)
	short_title = models.CharField(max_length=200)
	title = models.TextField(blank=True,null=True)
	pub_date = models.DateField(auto_now=False,auto_now_add=False, blank=True, null=True)
	pub_date_certainty = models.SmallIntegerField(choices=DATE_CERTAINTY_CHOICES, default=0)
	size = models.CharField(max_length=100, blank=True, null=True)
	physical_description = models.TextField(blank=True, null=True)
	tgm_genre = models.ForeignKey(TGM_Genre, models.SET_NULL, blank=True, null=True)
	other_description = models.TextField(blank=True, null=True)
	condition_notes = models.CharField(max_length=765, blank=True, null=True)
	edition = models.CharField(max_length=200, blank=True, null=True)
	original_source = models.ForeignKey(Original_Source, models.SET_NULL, blank=True, null=True)
	digitization_recommendation = models.CharField(max_length=20, choices=DIGITIZATION_CHOICES, blank=True, null=True)
	volume = models.CharField(max_length=50, blank=True, null=True)
	number = models.CharField(max_length=50, blank=True, null=True)
	record_status = models.CharField(max_length=20, choices=RECORD_STATUS_CHOICES)
	iona_holdings = models.CharField(max_length=20, choices=IONA_HOLDINGS_CHOICES, blank=True, null=True)
	pub_places = models.ManyToManyField(Location, blank=True)
	notes = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.short_title

#User editable list of Creator roles
#ex. author, editor, translator, printer, lithographer, etc
class Creator_Role(models.Model):
	name = models.CharField(max_length=200)
	notes = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.name


"""
Creators allows for an undeliminated number of people and organizations to be listed as creators
with their associated roles.

"""
class Item_Creator(models.Model):
	people = models.ManyToManyField(Person, blank=True)
	organizations = models.ManyToManyField(Organization, blank=True)
	items = models.ManyToManyField(Item)
	roles = models.ManyToManyField(Creator_Role)
	notes = models.TextField(blank=True, null=True)

	def __str__(self):
		return '%s %s %s %s' % (self.person, self.organization, self.item, self.role)

class Credit(models.Model):
	#Choice list used below
	TASK_CHOICES = [
		('created', 'created'),
		('enhanced', 'enhanced'),
		('reviewed', 'reviewed')
	]

	user = models.ForeignKey(User, models.PROTECT)
	item_record = models.ForeignKey(Item, models.PROTECT)
	task = models.CharField(max_length=20, choices=TASK_CHOICES)

	def __str__(self):
		return '%s %s' % (self.user, self.item_record)
