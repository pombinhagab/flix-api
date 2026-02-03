from django.contrib import admin
from django.urls import path
from genres.views import genres_create_list_view, genre_detail_view


urlpatterns = [
    path('admin/', admin.site.urls), # django admin
    path('genres/', genres_create_list_view, name='genres-create-list'), # get the list of genres
    path('genres/<int:pk>/', genre_detail_view, name='genre-detail-view') # one specific genre
]
