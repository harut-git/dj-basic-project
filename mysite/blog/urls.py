from django.conf.urls import url, include

import views

urlpatterns = [
    url(r'^index', views.home, name='home'),
    url(r'^about', views.about, name='about'),
    url(r'^categories', views.categories, name='categories')

]