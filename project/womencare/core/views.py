from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.views import APIView
from .models import React
from rest_framework.response import Response
from .serializer import ReactSerializer

# Create your views here.


class ReactView(APIView):
    serializer_class = ReactSerializer

    def get(self, request):
        data = []
        allData = React.objects.all().values("sex", "averageIncome", "averageSuper")
        for index, oneData in enumerate(allData):
            userInfo = {
                "id": index,
                "sex": oneData["sex"],
                "average_income": oneData["averageIncome"],
                "average_super": oneData["averageSuper"],
            }
            data.append(userInfo)

        return Response(data)

    def post(self, request):
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
