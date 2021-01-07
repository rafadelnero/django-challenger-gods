from rest_framework import serializers
from gods.models import God


class GodSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = God
        fields = ('id',
                  'name',
                  'power',
                  'greek')
