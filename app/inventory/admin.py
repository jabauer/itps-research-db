#inventory/admin.py

from django.contrib import admin

from inventory.models import Item, TGM_Genre, Original_Source, Creator_Role, Item_Creator, Credit

from organizations.models import Organization
from people.models import Person
from places.models import Location

#Register Models that exist to be editable lists
admin.site.register(TGM_Genre)
admin.site.register(Original_Source)

#Make Credit inline
class CreditInline(admin.TabularInline):
	model = Credit
	extra = 1

@admin.register(Creator_Role)
class Creator_RoleAdmin(admin.ModelAdmin):
	pass

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
	inlines = (CreditInline,)
	fieldsets = (
		(None, {
			'fields': (('accession_number','record_status'),'short_title','title',('pub_date','pub_date_certainty'),'pub_places',('edition','volume','number'),'other_description','original_source','notes')
		}),
		('Physical Object', {
			'classes': ('collapse',),
			'fields': ('tgm_genre','size','physical_description','condition_notes','digitization_recommendation','iona_holdings')
		})
	)

@admin.register(Item_Creator)
class Item_CreatorAdmin(admin.ModelAdmin):
	pass