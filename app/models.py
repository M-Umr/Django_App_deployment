from django.db import models

class Records(models.Model):
    Unnamed_0 = models.IntegerField()
    _id = models.CharField(max_length=1000, unique= True, blank=True, null=True)	
    Function = models.CharField(max_length=1000, blank=True, null=True)
    Time = models.DecimalField(max_digits=20, decimal_places=5)	
    Error = models.CharField(max_length=1000)	
    time_stamp = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.Unnamed_0