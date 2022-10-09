from django.db import models
from .models import Trainingvalue
class Topic(models.Model):
    name = models.CharField(max_length=200)


    firstweek= [type(u)*0.55, u*0.60, u*0.65]
    secondweek=[u*0.70,u*0.75,u*0.8]
    thirdweek=[u*0.8,u*0.85,u*0.9]
    a = f'Week 1 will consist of {sets1[0]}, {sets1[1]} sets of total reps {repsrange1[0]},{repsrange1[1]},at {firstweek[0]} kg,  {firstweek[1]}kg,{firstweek[2]}kg'
    b=  f'Week 2 will consist of {sets2[0]}, {sets2[1]} sets of total reps {repsrange2[0]},{repsrange2[1]} at {secondweek[0]} kg,  {secondweek[1]}kg,{secondweek[2]}kg'
    c=  f'Week 3 will consist of {sets3[0]}, {sets3[1]} sets of total reps {repsrange3[0]},{repsrange3[1]} at {thirdweek[0]} kg,  {thirdweek[1]}kg,{thirdweek[2]}kg'



class Trainingvalue(models.Model):
    maximalvalue= models.CharField(max_length=50)


class Word(models.Model):
    english = models.CharField( max_length=100)
    polish = models.CharField( max_length=100)
    genre = models.CharField( max_length=30)
    description = models.TextField(null=True,blank=True)
    updated = models.DateTimeField(auto_now=True)
    created= models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.id}:{self.english} - {self.polish}"


class Meta:
    ordering = ['-updated,-created']
