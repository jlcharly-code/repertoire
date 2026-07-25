from django.contrib import admin
from listings.models import Band, Listing

class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_formed', 'genre', 'active')  # Added 'active' for more info
    list_filter = ('genre', 'active')  # Added filters for genre and active status
    search_fields = ('name', 'biography')  # Enable search by name or biography

admin.site.register(Band, BandAdmin)

class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'band', 'created_at')  # Added 'created_at' if it exists
    list_filter = ('band',)  # Filter listings by band
    search_fields = ('title',)  # Search listings by title
    raw_id_fields = ('band',)  # Use raw ID widget for ForeignKey if needed

admin.site.register(Listing, ListingAdmin)

    
    