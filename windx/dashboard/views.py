from django.shortcuts import render

from models import QueryForm

def home(request):
    return render(request, 'dashboard.html')


def dashboard(request):
    form = QueryForm(request.GET)
    context = {'active_tab': 'dashboard', 'form': form}
    print request.GET.get('name')
    return render(request, 'dashboardTemplates/dashboard.html', context=context)


def user(request):
    context = {'active_tab': 'user'}
    return render(request, 'dashboardTemplates/user.html', context=context)
