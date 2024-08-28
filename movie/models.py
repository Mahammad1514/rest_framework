from django.db import models
from django.contrib.auth.models import User

# Create your models here.
LOCATION_CHOISES=[
    ('america','America'),
    ('asia','Asia'),
    ('europa','Europa'),

]   

class Studio(models.Model):
    title=models.CharField(max_length=30)
    location=models.CharField(max_length=20,choices=LOCATION_CHOISES)
    def __str__(self):
        return self.title
    
class Genre(models.Model):
    title=models.CharField(max_length=30)
    for_kids=models.BooleanField(default=True)

    def __str__(self):
        return self.title
    

class Movie(models.Model):
    title=models.CharField(max_length=50),
    genres=models.ManyToManyField(Genre,related_name='movies')
    studio=models.ForeignKey(Studio,on_delete=models.SET_NULL,null=True,blank=True)
    imdb=models.FloatField()
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    durations=models.IntegerField()
    release=models.DateField()
    local=models.BooleanField(default=False)
    updated=models.DateField(auto_now=True)
    created=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    


    

    
    





