from django.db import models


# Create your models here.
class GenderIncomeStats(models.Model):
    Sex = models.CharField(max_length=30, blank=True, null=True)
    State = models.CharField(max_length=30, blank=True, null=True)
    TaxableIncomeRange = models.CharField(max_length=300, blank=True, null=True)
    TaxableIncome = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        db_table = "gender_income_stats"
