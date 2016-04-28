"""
Models to capture sentiment
"""
from django.db import models
from twit.models import Tweet

class EntityMention(models.Model):
    tweet = models.ForeignKey(Tweet)
    doc_char_begin = models.IntegerField()
    doc_char_end = models.IntegerField()
    gloss = models.TextField()
    best_entity = models.TextField()

class TopicMention(models.Model):
    tweet = models.ForeignKey(Tweet)
    doc_char_begin = models.IntegerField()
    doc_char_end = models.IntegerField()
    gloss = models.TextField()
    best_entity = models.TextField()

