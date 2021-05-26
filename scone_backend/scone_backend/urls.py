from django.urls import include, path
from rest_framework import routers
from scone_backend_django_rest import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('schemes-list/', views.SchemesList, name="SchemesList"),
    path('schemes-add/', views.SchemesAdd, name="SchemesAdd"),
    path('opp-add/', views.OPPAdd, name="OPPAdd"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
