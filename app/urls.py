from django.contrib import admin
from django.urls import path
from genres.views import GenreCreateListView, GenreRetriveUpdateDestroyView
from actors.views import ActorCreateListView, ActorRetrieveUpdateDestroyView
from movies.views import MovieCreateListView, MovieRetriveUpdateDestroyView


urlpatterns = [
    path('admin/', admin.site.urls), # django admin
    
    
    path('genres/', GenreCreateListView.as_view(), name='genres-create-list'), 
    path('genres/<int:pk>/', GenreRetriveUpdateDestroyView.as_view(), name='genre-detail-view'),
     

    path('actors/', ActorCreateListView.as_view(), name='actors-create-list'),
    path('actors/<int:pk>/', ActorRetrieveUpdateDestroyView.as_view(), name='actors-detail-view'),


    path('movies/', MovieCreateListView.as_view(), name='movie-create-list'),
    path('movies/<int:pk>/', MovieRetriveUpdateDestroyView.as_view(), name='movie-detail-view'),
]
