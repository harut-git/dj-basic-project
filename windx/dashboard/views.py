from django.shortcuts import render


def home(request):
    return render(request, 'dashboard.html')


def dashboard(request):
    context = {'active_tab': 'dashboard'}
    return render(request, 'dashboardTemplates/dashboard.html', context=context)


def user(request):
    context = {'active_tab': 'user'}
    return render(request, 'dashboardTemplates/user.html', context=context)