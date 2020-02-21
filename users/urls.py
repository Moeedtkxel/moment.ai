
# from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path,re_path

from users import views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

# Create your urls here.
urlpatterns = [
    re_path(r'^users/$', views.UserList.as_view(), name='user-list'),
    re_path(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
    re_path(r'^register/$', views.AuthRegister.as_view(), name='register'),
    re_path(r'^login/', obtain_jwt_token),
    re_path(r'^token/refresh/', refresh_jwt_token),
    re_path(r'^token/verify/', verify_jwt_token)
]
