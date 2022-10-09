
from random import choices
from django.contrib.auth.models import User
from django.db import models

class profile(models.Model):
    user= models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name= models.CharField(max_length=100, null=True)
    waga= models.PositiveIntegerField(default=0, blank=True, null=True)
    wzrost = models.PositiveIntegerField(default=0, blank=True, null=True)
    # socialmediapage= models.Charfield(max_length=40, null=True)
    updated = models.DateTimeField(auto_now=True)

    created= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        
        return self.name

    def __str__(self):
        return self.waga

    def __str__(self):
        return self.name



class Meta:
    ordering = ['-updated,-created']



# class WEEKS(models.Model):
        
#     WEEK_1="1"
#     WEEK_2="2"
#     WEEK_3="3"
#     WEEK_4="4"
#     WEEK_CHOICES=[
#         (WEEK_1,"1"),
#         (WEEK_2,"2"),
#         (WEEK_3,"3"),
#         (WEEK_4,"4"),
#     ]
#     AccessoryWeek1=models.ManyToManyField(max_length=20,choices=WEEK_1)
#     AccessoryWeek2=models.ForeignKey(max_length=20,choices=WEEK_2)
#     AccessoryWeek3=models.ForeignKey(max_length=20,choices=WEEK_3)
#     AccessoryWeek4=models.ForeignKey(max_length=20,choices=WEEK_4)

class Trainingvalue(models.Model):

    UPPERBIEXERCISE_PULLUPS ="PULLUPS"
    UPPERBIEXERCISE_CHINUPS ="CHINUPS"
    UPPERBIEXERCISE_OVERHEADPRESS= "OVERHEADPRESS"
    UPPERBIEXERCISE_BARBELLROWS="BARBELLROWS"
    UPPERBIEXERCISE_TRXROWS="TRXROWS"
    UPPERBIEXERCISE_CHOICES=[
        (UPPERBIEXERCISE_PULLUPS, "PULLUPS"),
        (UPPERBIEXERCISE_CHINUPS,"CHINUPS"),
        (UPPERBIEXERCISE_OVERHEADPRESS, "OVERHEADPRESS"),
        (UPPERBIEXERCISE_BARBELLROWS, "BARBELLROWS"),
        (UPPERBIEXERCISE_TRXROWS,"TRXROWS"),
    ]

    UPPERUNIEXERCISE_BENTPRESS = "BENTPRESS"
    UPPERUNIEXERCISE_WINDMILL = "WINDMILL"
    UPPERUNIEXERCISE_ROWS="ROWS"
    UPPERUNIEXERCISE_CHOICES=[
        (UPPERUNIEXERCISE_BENTPRESS, "BENTPRESS"),
        (UPPERUNIEXERCISE_WINDMILL,"WINDMILL"),
        (UPPERUNIEXERCISE_ROWS,"ROWS"),
        ]

    LOWERBIEXERCISE_GLUTEBRIDGE="GLUTEBRIDGE"
    LOWERBIEXERCISE_SWING="SWING"
    LOWERBIEXERCISE_CHOICES=[
        (LOWERBIEXERCISE_GLUTEBRIDGE,"GLUTEBRIDGE"),
        (LOWERBIEXERCISE_SWING,"SWING"),
        ]

    LOWERUNIEXERCISE_LUNGES ="LUNGES"
    LOWERUNIEXERCISE_STEPUPS = "STEPUPS"
    LOWERUNIEXERCISE_BULGARIANSPLITSQUATS= "BULGARIANSPLITSQUATS"
    LOWERUNIEXERCISE_CHOICES=[
        (LOWERUNIEXERCISE_LUNGES, "LUNGES"),
        (LOWERUNIEXERCISE_STEPUPS,"STEPUPS"),
        (LOWERUNIEXERCISE_BULGARIANSPLITSQUATS,"BULGARIANSPLITSQUATS"),
        ]

    COREEXERCISE_RUSSIANTWIST="RUSSIANTWIST"
    COREEXERCISE_PLANK="PLANK"
    COREEXERCISE_REVERSEPLANK="REVERSEPLANK"
    COREEXERCISE_SIDEPLANK="SIDEPLANK"
    COREEXERCISE_CHOICES=[
        (COREEXERCISE_RUSSIANTWIST,"RUSSIANTWIST"),
        (COREEXERCISE_PLANK,"PLANK"),
        (COREEXERCISE_REVERSEPLANK,"REVERSEPLANK"),
        (COREEXERCISE_SIDEPLANK,"SIDEPLANK")
        ]

    WHOLEBODYEXERCISE_SLEDPUSH= "SLEDPUSH"
    WHOLEBODYEXERCISE_SLEDPULL="SLEDPULL"
    WHOLEBODYEXERCISE_TURKISHGETUP="TURKISHGETUP"
    WHOLEBODYEXERCISE_CHOICES=[
        (WHOLEBODYEXERCISE_SLEDPUSH, "SLEDPUSH"),
        (WHOLEBODYEXERCISE_SLEDPUSH, "SLEDPULL"),
        (WHOLEBODYEXERCISE_SLEDPUSH, "TURKISHGETUP"),
    ]
    MESOCYCLE_GPP= "GPP"
    MESOCYCLE_ACC= "ACC"
    MESOCYCLE_PEAK= "PEAK"
    MESOCYCLE_CASUALTRAINING= "CASUALTRAINING"
    MESOCYCLE_CHOICES=[
        (MESOCYCLE_GPP, "GPP"),
        (MESOCYCLE_ACC, "ACC"),
        (MESOCYCLE_PEAK, "PEAK"),
        (MESOCYCLE_CASUALTRAINING, "CASUALTRAINING")
    ]

    SETS_1="1"
    SETS_2="2"
    SETS_3="3"
    SETS_4="4"
    SETS_5="5"
    SETS_CHOICES=[
        (SETS_1, "1"),
        (SETS_2,"2"),
        (SETS_3,"3"),
        (SETS_4,"4"),
        (SETS_5,"5"),
    ]

    REPS_3="3"
    REPS_5="5"
    REPS_8="8"
    REPS_10="10"
    REPS_13="13"
    REPS_20="20"
    REPS_AMRAP="AMRAP"
    REPS_CHOICES=[
        (REPS_3,"3"),
        (REPS_5,"5"),
        (REPS_8,"8"),
        (REPS_10,"10"),
        (REPS_13,"13"),
        (REPS_20,"20"),
        (REPS_AMRAP,"AMRAP")
    ]
    

    
    upperbodbi= models.CharField(verbose_name="Upper body bilateral exercise accessory",max_length=20,choices=UPPERBIEXERCISE_CHOICES,default=UPPERBIEXERCISE_PULLUPS)
    upperbodybisets= models.CharField(verbose_name="Upper body bilateral exercise sets",max_length=20,choices=SETS_CHOICES,default=SETS_1)
    upperbodybireps= models.CharField(verbose_name="Upper body bilateral exercise reps",max_length=20,choices=REPS_CHOICES,default=REPS_8)

    upperboduni = models.CharField(verbose_name="Upper body unilateral exercise accessory",max_length=20,choices=UPPERUNIEXERCISE_CHOICES,default=UPPERUNIEXERCISE_ROWS)
    upperbodyunisets= models.CharField(verbose_name="Upper body unilateral exercise sets",max_length=20,choices=SETS_CHOICES,default=SETS_1)
    upperbodyunireps= models.CharField(verbose_name="Upper body unilateral exercise reps",max_length=20,choices=REPS_CHOICES,default=REPS_8)

    lowerbodybi= models.CharField(verbose_name="Lower body bilateral exercise accessory",max_length=20,choices=LOWERBIEXERCISE_CHOICES,default=LOWERBIEXERCISE_SWING)
    lowerbodybisets= models.CharField(verbose_name="Lower body bilateral exercise sets",max_length=20,choices=SETS_CHOICES,default=SETS_1)
    lowerbodybireps= models.CharField(verbose_name="Lower body bilateral exercise reps",max_length=20,choices=REPS_CHOICES,default=REPS_8)

    lowerbodyuni= models.CharField(verbose_name="Lower body unilateral exercise accessory",max_length=20,choices=LOWERUNIEXERCISE_CHOICES,default=LOWERUNIEXERCISE_BULGARIANSPLITSQUATS)
    lowerbodyunisets= models.CharField(verbose_name="Lower body unilateral exercise sets",max_length=20,choices=SETS_CHOICES,default=SETS_1)
    lowerbodyunireps= models.CharField(verbose_name="Lower body unilateral exercise reps",max_length=20,choices=REPS_CHOICES,default=REPS_8)

    coretraining=  models.CharField(verbose_name="Core body exercise",max_length=20, choices=COREEXERCISE_CHOICES,default=COREEXERCISE_RUSSIANTWIST)
    coresets= models.CharField(verbose_name="Core sets",max_length=20,choices=SETS_CHOICES,default=SETS_1)
    corereps= models.CharField(verbose_name="Core reps",max_length=20,choices=REPS_CHOICES,default=REPS_8)

    wholebodyexercise =  models.CharField(verbose_name="Exercise engaging all segments of body",max_length=20,choices=WHOLEBODYEXERCISE_CHOICES,default=WHOLEBODYEXERCISE_TURKISHGETUP)
    wholebodysets = models.CharField(verbose_name="Whole body exercise sets",max_length=20,choices=SETS_CHOICES,default=SETS_1)
    wholebodyreps = models.CharField(verbose_name="Whole body exercise reps",max_length=20,choices=REPS_CHOICES,default=REPS_8)
    


    
    SQUAT1RM= models.PositiveIntegerField(verbose_name="100% maximal repetition in squat",default=0, blank=True, null=True)
    DEADLIFT1RM=models.PositiveIntegerField(verbose_name="100% maximal repetition in deadlift",default=0, blank=True, null=True)
    BENCHPRESS1RM= models.PositiveIntegerField(verbose_name="100% maximal repetition in benchpress",default=0, blank=True, null=True)
    
    #ATHLETIC
    mesocycle= models.CharField(max_length=20, choices=MESOCYCLE_CHOICES,default=MESOCYCLE_GPP)
    updated = models.DateTimeField(auto_now=True)
    created= models.DateTimeField(auto_now_add=True)

    user= models.ForeignKey(User,null=True,verbose_name="Username", on_delete=models.CASCADE)

 

    # def __str__(self):
    #     return self.user


    # def __str__(self):
        
    #     return str(self.SQUAT1RM),str(self.DEADLIFT1RM),


    # def __innit__(self):
    #     return self.mesocycle

    # def __innit__(self):
    #     return str(self.upperbodbi), str(self.upperboduni), str(self.lowerbodybi), str(self.lowerbodyuni), str(self.coretraining) ,str(self.wholebodyexercise)
   
class Word(models.Model):
    
    english = models.CharField( max_length=100)
    polish = models.CharField( max_length=100)
    genre = models.CharField( max_length=30)
    description = models.TextField(null=True,blank=True)
    updated = models.DateTimeField(auto_now=True)
    created= models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.id}:{self.english} - {self.polish}"

  

