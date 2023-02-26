import datetime

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

# Create your models here.
# Model is the single deifnitive source of truth about ou data
# It contains the essential fields and behaviors of the data we are storing
# Migrations are derived from models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now()-datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default = 0)
    def __str__(self):
        return self.choice_text


# each model is represented by a class that subclasses
# django.db.models.Model
# each model has a anumber of class variables, each of which
# represents a database field in the model

# Each field is represented by an instance of a Field class
# CharField for character field, DateTImeField for datetimes
# this tells django what type of data each field holds

# the name of each Field instance (e.g question_text or pub_date)
# is the fields name in machine_friendly format
# we can use optional first positional argument to a Field
# to designate human-readable name.

# Some Field classes have required arguments.
# CharField requires that you it a max_length
# its usend in the database schema but also in validation

# Field can have various optional arguments
# like default argument of votes set to 0

# relationship is defind using ForeignKey
# it tells Django that choice is related to singe Question
# Django support all the common database relationships:
# many-to-one, many-to-many, one-to-one.

# Activating models
# model code give Django information
# Django then creates a database schema (create table for this app)
# create a python database-acces API for accesing Question and Choice objects
# first we need to tell our project that the polls app is installed

# django apps are pluggable and can be used in multiple projects