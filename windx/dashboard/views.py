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


def results(request):
    db_results = {}
    k = 'in' + request.GET.get('name')
    employee = Employee.objects.filter(entry_id=k)
    for i in employee:
        db_results.update({i.date: i.entry_id})
    context = {'results': db_results}
    return render(request, 'dashboardTemplates/results.html', context=context)
