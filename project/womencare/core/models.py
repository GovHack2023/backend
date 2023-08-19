from django.db import models


# Create your models here.
class React(models.Model):
    sex = models.CharField(max_length=30, blank=True, null=True)
    averageIncome = models.IntegerField(blank=True, null=True)
    averageSuper = models.IntegerField(blank=True, null=True)
