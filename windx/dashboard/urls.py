from django.conf.urls import url, include

import views

urlpatterns = [
    url(r'^dashboard', views.dashboard, name='dashboard'),
    url(r'^user', views.user, name='user'),
    url(r'^index', views.index, name='index')

]