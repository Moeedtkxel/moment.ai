from .views import DisplayAllCameras
from django.conf.urls import url

urlpatterns = [
    url(r'^cameras/$', DisplayAllCameras.as_view(), name='cameras-allrud')
]
