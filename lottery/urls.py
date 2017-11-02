from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import LotteryViewSet

lottery_list = LotteryViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

lottery_detail = LotteryViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
    url(r'^lottery$', lottery_list, name='lottery_list'),
    url(r'^lottery/(?P<pk>[0-9]+)/$', lottery_detail, name='lottery_detail'),
])