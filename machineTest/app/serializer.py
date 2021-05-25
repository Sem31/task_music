from mutagen import mp3
from rest_framework import serializers
from .models import SongDetail
from mutagen.mp3 import MP3

class SongUploaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SongDetail
        fields = '__all__'
        read_only_fields = ('song_duration',)

    def create(self, validated_data):
        file = validated_data['upload_song'].temporary_file_path()
        duration = MP3(file).info.length
        user_obj = SongDetail(
            song_name=validated_data['song_name'],
            song_duration=duration,
            upload_song=validated_data['upload_song']
        )
        user_obj.save()
        return user_obj