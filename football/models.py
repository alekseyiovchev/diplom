from django.db import models

# Create your models here.
class Scores(models.Model):
    id = models.IntegerField(primary_key=True)
    first_team = models.CharField(max_length=30)
    first_team_icon = models.URLField(max_length = 200,default='null')
    second_team = models.CharField(max_length=30)
    second_team_icon = models.URLField(max_length = 200,default='null')
    match_date = models.DateTimeField()
    score_first_team = models.IntegerField(default=0)
    score_second_team = models.IntegerField(default=0)

class Players(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    bio = models.TextField()
    date_of_birth = models.DateTimeField()
    nationality = models.CharField(max_length=30)
    current_team = models.CharField(max_length=30)
    first_team = models.CharField(max_length=30)
    first_team_icon = models.URLField(max_length = 200,default='null')
    second_team = models.CharField(max_length=30)
    second_team_icon = models.URLField(max_length = 200,default='null')
    match_date = models.DateTimeField()
    score_first_team = models.IntegerField(default=0)
    score_second_team = models.IntegerField(default=0)