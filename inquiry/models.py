from django.db import models

#this is a comment
class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)  
    def __unicode__(self):
        return u'%s %s' (self.first_name, self.last_name)        

EVENT_CHOICES = (
('Q', 'Question'),
('P', 'Prediction'),
('O', 'Observation'),
('E', 'Explanation'),
('M', 'Model'),
)

class Event (models.Model):
    pub_date = models.DateTimeField('datepublished')
    author = models.ForeignKey(Author)
    referants = models.ForeignKey('Event')
    event_type = models.CharField(max_length=1, choices=EVENT_CHOICES)
    description = models.CharField(max_length=300)
    #tag = models.ManyToManyField(Tag) # FIXME
    def __unicode__(self):
        return self.event_type + u'. '  + self.description
        
               

    
# Create your models here.
