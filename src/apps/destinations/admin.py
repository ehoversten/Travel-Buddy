from django.contrib import admin

from .models import Destination

class DestinationAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'location', 'description', 'completed')
    # Renders the content with an href
    list_display_links = ('id', 'location')
    list_filter = ('planner',)  #comma since it is a tuple
    list_editable = ('completed',)
    search_fields = ('location', 'description', 'planner')
    list_per_page = 25


admin.site.register(Destination, DestinationAdmin)