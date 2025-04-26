from django.db.models import Avg
from rest_framework import serializers
from artists.serializers import ArtistSerializer
from genres.serializers import GenreSerializer
from songs.models import Song


class SongModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = '__all__'

    def validate_release_date(self, value):
        if value.year < 1945:
            raise serializers.ValidationError('A data de lançamento da música não poder ser inferior a 1945')
        return value

    def validate_resume(self, value):
        if len(value) > 500:
            raise serializers.ValidationError('Resumo não pode ser maior que 300 caracteres.')
        return value


class SongListDetailSerializer(serializers.ModelSerializer):
    artists = ArtistSerializer(many=True)
    genre = GenreSerializer()
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Song
        fields = ['id', 'title', 'genre', 'artists', 'release_date', 'rate', 'resume']

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 1)
        return None
