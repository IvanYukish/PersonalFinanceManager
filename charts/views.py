from Transactions.models import Transactions
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from Transactions.forms import GenereteReport

from rest_framework.views import APIView
from rest_framework.response import Response


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts.html', {"customers": 10})


def get_data(request, *args, **kwargs):
    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data)  # http response


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        labels = []
        default_items = []
        transacts = Transactions.objects.all()
        for transact in transacts:
            labels.append(transact.category.name)
            default_items.append(int(transact.suma))
        data = {
            "labels": labels,
            "default": default_items,
        }
        return Response(data)

def getReportdata(request):
    form = GenereteReport()
    # model = Transactions.objects.all()
    # report = Transactions.objects.filter(created='2012/09/01')
    # print(report.query)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'generateReport.html', {'form': form})
