from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions


@api_view(['GET', ])
@permission_classes((permissions.AllowAny,))
def api_homepage_view(request, format=None):
    return Response({
        'rooms': reverse('api_rooms:home', request=request, format=format),
        'customers': reverse('api_customers:home', request=request, format=format),
        'reservations': reverse('api_reservations:home', request=request, format=format),
        'login': reverse('token_obtain_pair', request=request, format=format),
        'refresh': reverse('token_refresh', request=request, format=format),

    })