
from django.db import models
from datetime import datetime



class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    age=models.CharField(max_length=2)
    role=models.CharField(max_length=20)
    
    reviews=models.TextField()
    prediction_result = models.CharField(max_length=100,default='default_value')
    sentimentscore = models.FloatField(default=0.0)
    
    
    date =models.DateField()

    def __str__(self):
        return self.name
        
    
