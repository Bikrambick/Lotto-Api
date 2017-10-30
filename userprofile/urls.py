from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import UserViewSet

user_list = UserViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

user_detail = UserViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
    url(r'^users$', user_list, name='user_list'),
    url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user_detail'),
])
