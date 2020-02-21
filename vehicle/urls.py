from django.conf.urls import url

from vehicle.views import DisplayAllVehicles

urlpatterns = [
    url(r'^vehicles/$', DisplayAllVehicles.as_view(), name='cameras-allrud')
]
