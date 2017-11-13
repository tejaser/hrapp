from django.db import models
from django.utils import timezone

# Create your models here.

class Candidate(models.Model):
    author = models.ForeignKey('auth.User')
    fName = models.CharField(max_length=50)
    lName = models.CharField(max_length=50)
    mName = models.CharField(max_length=50, blank=True, default=' ')
    email = models.EmailField(max_length=254)
    mobile = models.CharField(max_length=20)
    highestQualification = models.CharField(max_length=200)
    jobPosition = models.CharField(max_length=200)
    consultancy = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.update_date = timezone.now()
        self.save()

    def __str__(self):
        return (self.fName + ' ' + self.mName + ' ' +self.lName)
