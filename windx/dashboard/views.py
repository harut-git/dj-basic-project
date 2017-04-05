import re

from django.shortcuts import render

from models import UserId
from models import Employee


def home(request):
    return render(request, 'dashboard.html')


def dashboard(request):
    context = {'active_tab': 'dashboard'}
    print request.GET.get('name')
    return render(request, 'dashboardTemplates/dashboard.html', context=context)


def user(request):
    context = {'active_tab': 'user'}
    return render(request, 'dashboardTemplates/user.html', context=context)


def index(request):
    k = UserId.objects.all()
    users = {}
    for i in k:
        users.update({i.name: i.user_id})
    print users
    context = {'users': users}
    return render(request, 'dashboardTemplates/datetime.html', context=context)


def find_key(input_dict, value):
    return next((k for k, v in input_dict.items() if v == value), None)


def results(request):
    db_results = {}
    k = UserId.objects.all()
    users = {}
    for i in k:
        users.update({i.name: i.user_id})
    print users
    # k = 'in' + request.GET.get('name')
    employee = Employee.objects.all()
    for j in employee:
        if j.entry_id in users.values():
            date = j.day + '-' + j.month + '--' + j.hour + ':' + j.minute
            db_results.update({date: find_key(users, j.entry_id) + '-' + j.action})
    context = {'results': db_results}
    return render(request, 'dashboardTemplates/results.html', context=context)
