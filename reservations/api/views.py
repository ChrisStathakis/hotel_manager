from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.reverse import reverse

from django_filters.rest_framework import DjangoFilterBackend

from .serializers import ReservationListSerializer, ReservationUpdateSerializer
from .serializers import Reservation


@api_view(['GET', ])
def reservations_homepage_view(request, format=None):

    return Response({
        'list': reverse('api_reservations:list', request=request, format=format)
    })


class ReservationListCreateApiView(ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationListSerializer
    permission_classes = [IsAuthenticated, ]
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['customer', 'room', 'isDone', 'isCancel', ]
    search_fields = ['title', 'room', 'customer']


class ReservationRetrieveUpdateDeleteApiView(RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationUpdateSerializer

