from django.db import models


# Create your models here.
class IndustryIncome(models.Model):
    Industry = models.CharField(max_length=300, blank=True, null=True)
    Total = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        db_table = "gender_industry_income_count"
