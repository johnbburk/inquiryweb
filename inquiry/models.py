from django.db import models

#this is a comment

# use http://code.google.com/p/django-tagging/ or something else for tagging?
class Author(models.Model):
    firstName = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)
    # email address?
    # adorable picture?
    def __unicode__(self):
        return self.firstName + u” ” + self.lastName

EVENT_CHOICES = (
(‘Q’, ‘Question’),
(‘P’, ‘Prediction’),
(‘O’, ‘Observation’),
(‘E’, ‘Explanation’),
(‘M’, ‘Model’),
)

class Event (models.Model):
    pub_date = models.DateTimeField(‘datepublished’)
    author = models.ForeignKey(Author)
    referants = models.ManyToMany(Event)
    event_type = models.CharField(max_length=1, choices=EVENT_CHOICES)
    description = models.CharField(max_length=300)
    tag = models.ManyToManyField(Tag) # FIXME
    def __unicode__(self):
        return self.event_type + u”. ” + self.description
    
# Create your models here.
