from rest_framework import serializers

from ..models import GenericExpense, Bill, BillCategory, Occupation, Person, Payroll



class PersonSerializer(serializers.ModelSerializer):
    queryset = Person.objects.all()