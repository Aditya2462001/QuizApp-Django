from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Subject(models.Model):
    name = models.CharField( max_length=50)


    def __str__(self):
        return self.name

class Question(models.Model):
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    question = models.CharField(max_length=1000)
    option_1 = models.CharField(max_length=500, null= True , blank=True , default="Non of the above")
    option_2 = models.CharField(max_length=500, null= True , blank=True , default="Non of the above")
    option_3 = models.CharField(max_length=500, null= True , blank=True , default="Non of the above")
    option_4 = models.CharField(max_length=500, null= True , blank=True , default="Non of the above")
    answer = models.CharField(max_length=50,default="any of them" )

    def __str__(self):
        return self.question




