from django.db import models

# Create your models here.
class Scores(models.Model):
    id = models.IntegerField(primary_key=True)
    first_team = models.CharField(max_length=30)
    second_team = models.CharField(max_length=30)
    match_date = models.DateTimeField()
    score = models.CharField(max_length=5)