from django.urls import path
from . import views


urlpatterns = [
    path('artists/', views.ArtistCreateListView.as_view(), name='artist-create-list'),
    path('artists/<int:pk>/', views.ArtistRetrieveUpdateDestroyView.as_view(), name='artist-detail-view'),
]
