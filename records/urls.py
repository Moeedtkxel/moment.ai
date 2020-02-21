from .views import DisplayAllRecords
from django.conf.urls import url

urlpatterns = [
    url(r'^records/$', DisplayAllRecords.as_view(), name='records-allrud')
]
