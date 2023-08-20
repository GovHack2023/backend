from django.urls import path
from .views import *

urlpatterns = [
    path("womenCare", womenCare, name="womenCare"),
    path("genderIncome", genderIncome, name="genderIncome"),
    path("industryIncome", industryIncome, name="industryIncome"),
]
