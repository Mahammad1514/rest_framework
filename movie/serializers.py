from rest_framework import serializers
from .models import Studio, Genre, Movie

class StudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Studio
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre         
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    studio=StudioSerializer(read_only=True)
    genres=GenreSerializer(many=True, read_only=True)   
    studio_id=serializers.IntegerField(write_only=True) 
    genres_ids=serializers.ListField(write_only=True, source='genres')
    class Meta:
        model = Movie 
        fields = '__all__'     

def validate_imdb(self, value):
    if not 1 <= value <= 10:
        raise serializers.ValidationError(
                "IMDB can be between 1 and 10")
    return value
