from django.db.models import Count, Avg
from rest_framework import generics, views, response, status
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from songs.models import Song
from songs.serializers import SongModelSerializer, SongListDetailSerializer
from reviews.models import Review


class SongCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Song.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SongListDetailSerializer
        return SongModelSerializer


class SongRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Song.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SongListDetailSerializer
        return SongModelSerializer


class SongStatsView(views.APIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Song.objects.all()

    def get(self, request):
        # Buscar todos os dados
        total_songs = self.queryset.count()
        songs_by_genre = self.queryset.values('genre__name').annotate(count=Count('id'))
        total_reviews = Review.objects.count()
        average_stars = Review.objects.aggregate(avg_stars=Avg('stars'))['avg_stars']
        # Montar respostas
        # Devolver respostas para o usuário com estatísticas
        return response.Response(data={
            'total_songs': total_songs,
            'songs_by_genre': songs_by_genre,
            'total_reviews': total_reviews,
            'average_stars': round(average_stars, 1) if average_stars else 0,
        }, status=status.HTTP_200_OK)
