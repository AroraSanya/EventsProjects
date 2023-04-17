from django.contrib import admin
from .models import Event,Join_events
class EventAdmin(admin.ModelAdmin):
    model = Event
    list_display = ('title', 'description','start_datetime','end_datetime')
class Join_eventsAdmin(admin.ModelAdmin):
    model = Join_events
    list_display = ('event',)
admin.site.register(Event,EventAdmin)
admin.site.register(Join_events,Join_eventsAdmin)