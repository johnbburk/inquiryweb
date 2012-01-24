from django.db import models

#this is a comment
class Author(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    
class Question (models.Model):
    question = models.CharField(max_length=300)
    pub_date = models.DateTimeField('datepublished')
    author = models.ForeignKey(Author)
    
class Prediction (models.Model):
    prediction = models.CharField(max_length=300)
    pub_date = models.DateTimeField('datepublished')
    author = models.ForeignKey(Author)
    
class Observation (models.Model):
    observation = models.CharField(max_length=300)
    pub_date = models.DateTimeField('datepublished')
    author = models.ForeignKey(Author)
    
class Answer (models.Model):
    Answer = models.CharField(max_length=300)
    pub_date = models.DateTimeField('datepublished')
    author = models.ForeignKey(Author)
               
    
# Create your models here.
