from django.contrib.auth.decorators import login_required

from Transactions.models import Transactions
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from Transactions.forms import GenereteReport
from Categories.forms import MyUserCreationForm

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
        form = GenereteReport(request.GET)
        if form.is_valid():
            old_date = form.cleaned_data['olddate']
            new_date = form.cleaned_data['newdate']
            categopy = form.cleaned_data['category']
            transacts = Transactions.objects.filter(created__gte=old_date, created__lte=new_date)
            for transact in transacts:
                labels.append(transact.category.name)
                default_items.append(int(transact.suma))
        else:
            print(form.errors)
        data = {
            "labels": labels,
            "default": default_items,
        }
        return Response(data)


@login_required
def getReportdata(request):
    form = GenereteReport()
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'generateReport.html', {'form': form})


def register(request):
    form = MyUserCreationForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('login')
    return render(request, 'registration/registr.html', {'form': form})
