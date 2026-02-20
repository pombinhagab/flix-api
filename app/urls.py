from django.contrib import admin
from django.urls import path
from genres.views import GenreCreateListView, GenreRetriveUpdateDestroyView


urlpatterns = [
    path('admin/', admin.site.urls), # django admin
    
    path('genres/', GenreCreateListView.as_view(), name='genres-create-list'), # all genres
    path('genres/<int:pk>/', GenreRetriveUpdateDestroyView.as_view(), name='genre-detail-view') # one specific genre
]
