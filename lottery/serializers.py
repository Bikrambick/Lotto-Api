from rest_framework import serializers 
from .models import Lottery

class LotterySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Lottery
        fields = ('id',  'url', 'name', 'number_balls', 'total_number_balls', 'date')