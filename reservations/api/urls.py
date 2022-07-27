from django.urls import path


from .views import (
    reservations_homepage_view,
    ReservationListCreateApiView,
    ReservationRetrieveUpdateDeleteApiView
)

app_name = 'api_reservations'

urlpatterns = [
    path('', reservations_homepage_view, name='home'),
    path('list/', ReservationListCreateApiView.as_view(), name='list'),
    path('detail/<int:pk>/', ReservationRetrieveUpdateDeleteApiView.as_view(), name='update')
]