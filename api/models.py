from django.db import models
import datetime
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class BookJournalBase(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    price = models.IntegerField()
    decription = models.CharField(max_length=512, blank=False, null=False)
    created_at = models.DateField(default=datetime.date.today)

class Book(BookJournalBase):
    num_pages = models.IntegerField()
    genre = models.PositiveSmallIntegerField(choices=[(0, "HORROR"), (1, "ROMATIC"), (2, "DETECTIVE"), (3, "MAFIA")])

class Journal(BookJournalBase):
    type = models.PositiveSmallIntegerField(choices=[(0, "BULLET"), (1, "FOOD"), (2, "TRAVEL"), (3, "SPORT")])
    publisher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)