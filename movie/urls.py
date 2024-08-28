from django.urls import path
from . import views 

urlpatterns = [ 
    path('movie-list/',views.MovieListAV.as_view(),name='movie-list'),
    path('movie-list/<int:pk>',views.MovieDetailAV.as_view(),name='movie-detail'),
    path('genre-list/',views.GenreListAV.as_view(),name='genre-list'),
    path('genre-list/<int:pk>',views.GenreDetailAV.as_view(),name='genre-detail'),
    path('studio-list/',views.StudioListAV.as_view(),name='studio-list'),
    path('studio-list/<int:pk>',views.StudioDetailAV.as_view(),name='studio-detail'),

]

    
