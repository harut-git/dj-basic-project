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
    r = re.compile("([a-zA-Z]+)([0-9]+)")
    db_results = {}
    k = UserId.objects.all()
    users = {}
    for i in k:
        users.update({i.name: i.user_id})
    print users
    # k = 'in' + request.GET.get('name')
    employee = Employee.objects.all()
    for j in employee:
        m = r.match(j.entry_id)
        action = m.group(1)
        clear_id = m.group(2)
        if clear_id in users.values():
            db_results.update({j.date: find_key(users, clear_id)+'---'+action})
        # db_results.update({j.date: j.entry_id})
    context = {'results': db_results}
    return render(request, 'dashboardTemplates/results.html', context=context)
