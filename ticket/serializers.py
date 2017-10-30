from rest_framework import serializers
from .models import Ticket

class TicketSerializer(serializers.HyperlinkedModelSerializer):

    class class Meta:
        model = Ticket
