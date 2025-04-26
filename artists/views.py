from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from artists.models import Artist
from artists.serializers import ArtistSerializer


class ArtistCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class ArtistRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
