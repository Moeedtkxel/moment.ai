from .views import DisplayAllDrivers
from django.conf.urls import url

urlpatterns = [
    url(r'^drivers/$', DisplayAllDrivers.as_view(), name='cameras-allrud')
]
