from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from ..models import Reservation


class ReservationListSerializer(ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api_reservations:update')

    class Meta:
        model = Reservation
        fields = [
            'id', 'room', 'customer', 'source', 'check_in', 'check_out', 'checkIn', 'capacity',
            'isCancel', 'isDone', 'clean_value', 'extra_cost_per_person', 'value',
            'charges_value', 'discount', 'days', 'final_value', 'date_range', 'active_status', 'str_status',
            'str_customer', 'str_room', 'extra_cost_per_person', 'clean_value', 'url', 'str_room_day_price',
            'str_extra_price_per_day', 'str_color'
        ]

    def validate(self, data):
        if data['check_in'] > data['check_out']:
            raise serializers.ValidationError('Date Problem')
        qs = Reservation.objects.filter(check_in__in=[data['check_in'], data['check_out']],
                                        room=data['room'], isCancel=False, isDone=False)
        if qs.exists():
            raise serializers.ValidationError('The is a exist reservation on this room')
        return data


class ReservationUpdateSerializer(ModelSerializer):

    class Meta:
        model = Reservation
        fields = [
            'id', 'room', 'customer', 'source', 'check_in', 'check_out', 'checkIn', 'capacity',
            'isCancel', 'isDone', 'clean_value', 'extra_cost_per_person', 'value',
            'charges_value', 'discount', 'days', 'final_value', 'date_range', 'active_status', 'str_status',
            'str_customer', 'str_room', 'extra_cost_per_person', 'clean_value', 'str_room_day_price',
            'str_extra_price_per_day'
        ]