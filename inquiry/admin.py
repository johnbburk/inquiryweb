from django.contrib import admin
from models import Event


class EventAdmin(admin.ModelAdmin):
    list_display= ('id', 'author', 'event_type', 'description')
    fieldsets = [
        (None, {'fields': ['referants']}),
    ('Inquiry Event', {'fields': ['event_type','description']}),
        ]
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
                obj.author=request.user
        obj.save()
        
            
admin.site.register(Event, EventAdmin)