from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse, reverse_lazy
from rest_framework.permissions import IsAuthenticated

@api_view(['GET', 'POST'])
#@permission_classes((IsAuthenticated,))
def api_root(request, format=None):
    return Response({
    	'users': reverse('users:user_list', request=request, format=format),
        'lottery' : reverse('lottery:lottery_list', request= request, format=format),
    })

from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter

    