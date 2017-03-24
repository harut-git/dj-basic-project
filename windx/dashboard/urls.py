from django.conf.urls import url, include

import views

urlpatterns = [
    url(r'^index', views.home, name='home'),
    url(r'^dashboard', views.dashboard, name='dashboard'),
    url(r'^user', views.user, name='user')

]