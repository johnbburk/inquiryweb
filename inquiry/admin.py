from django.contrib import admin
from models import Author
from models import Event

admin.site.register(Author)


class EventAdmin(admin.ModelAdmin):
    fields=['description','event_type','author','pub_date','referants']
admin.site.register(Event, EventAdmin)