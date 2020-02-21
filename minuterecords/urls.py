from .views import DisplayMinuteRecordsById, DisplayDriverData, DisplayRecentIncidents
from django.conf.urls import url

urlpatterns = [
    url(r'^recordsbyid/$', DisplayMinuteRecordsById.as_view(), name='records-allrud'),
    url(r'^driverrecords/$', DisplayDriverData.as_view(), name='driver-allrud'),
    url(r'^recentincidents/$', DisplayRecentIncidents.as_view(), name='recent-allrud')

]
