from django.contrib import admin

from listings.models import Band

class BandAdmin(admin.ModelAdmin):
# we insert these two lines…
   list_display = ('name', 'year_formed', 'genre') 
   # list the fields we want on the list display

admin.site.register(Band, BandAdmin) 
# we edit this line, adding a second argument