from django.conf.urls import url
from AdminApp import views

urlpatterns=[
    url(r'^workstation/$',views.workstationApi),
    url(r'^workstation/([0-9]+)$', views.workstationApi),
]