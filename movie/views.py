from django.shortcuts import render 
from .models import Studio, Movie, Genre
from .serializers import StudioSerializer, MovieSerializer, GenreSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.

class MovieListAV(ListCreateAPIView): 
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer 

class MovieDetailAV(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer 


class GenreListAV(ListCreateAPIView):        
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer 

class GenreDetailAV(RetrieveUpdateDestroyAPIView):        
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer 


class StudioListAV(ListCreateAPIView):
    queryset = Studio.objects.all()
    serializer_class = StudioSerializer 

class StudioDetailAV(RetrieveUpdateDestroyAPIView):
    queryset = Studio.objects.all()
    serializer_class = StudioSerializer 
