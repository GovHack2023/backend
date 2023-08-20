from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.views import APIView
from .models import React
from .genderIncomeStats import GenderIncomeStats
from rest_framework.response import Response
from django.http import HttpRequest, JsonResponse

# Create your views here.


def womenCare(request):
    dataSend = []
    allData = React.objects.all().values("sex", "averageIncome", "averageSuper")
    for index, oneData in enumerate(allData):
        userInfo = {
            "id": index,
            "sex": oneData["sex"],
            "average_income": oneData["averageIncome"],
            "average_super": oneData["averageSuper"],
        }
        dataSend.append(userInfo)
    response = JsonResponse(status=200, data={"data": dataSend})
    return response


def genderIncome(request):
    dataSend = []
    allData = GenderIncomeStats.objects.all().values(
        "Sex", "State", "TaxableIncomeRange", "TaxableIncome"
    )
    for index, oneData in enumerate(allData):
        userInfo = {
            "id": index,
            "sex": oneData["Sex"],
            "state": oneData["State"],
            "TaxableIncomeRange": oneData["TaxableIncome"],
        }
        dataSend.append(userInfo)
    response = JsonResponse(status=200, data={"data": dataSend})
    return response
