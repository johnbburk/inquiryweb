from django.db import models
from django.contrib.auth.models import User
import tagging 
from django.forms import ModelForm


EVENT_CHOICES = (
('Q', 'Question'),
('P', 'Prediction'),
('O', 'Observation'),
('E', 'Explanation'),
('M', 'Model'),
)

class Event (models.Model):
    add_datetime = models.DateTimeField('Created', auto_now_add=True)
    mod_datetime = models.DateTimeField('Modified', auto_now=True)
    author = models.ForeignKey(User, null=True, blank=True)
    referants = models.ManyToManyField('self', symmetrical=False, blank = True, null=True)
    event_type = models.CharField('I have a' , max_length=1, choices=EVENT_CHOICES)
    description = models.CharField(max_length=300)
    #tag = models.ManyToManyField(Tag) # FIXME
    def __unicode__(self):
        return (u'%s. %s'%(self.event_type,self.description))
        
#tagging.register(Event)

class EventForm(ModelForm)
     class Meta:
         model = Event 
    