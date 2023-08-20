from django.db import models


# Create your models here.
class GenderIncomeStats(models.Model):
    sex4 = models.CharField(max_length=30, blank=True, null=True)
    state = models.CharField(max_length=30, blank=True, null=True)
    taxIncome = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        db_table = "gender_income_stats"
