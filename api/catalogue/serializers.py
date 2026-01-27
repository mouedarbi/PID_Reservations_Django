from rest_framework import serializers
from catalogue.models import Artist

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artist
        fields = ['url', 'id', 'firstname', 'lastname']