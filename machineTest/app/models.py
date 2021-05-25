from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
class SongDetail(models.Model):
    song_name = models.CharField(max_length=100)
    song_duration = models.IntegerField(blank=True,null=True)
    upload_song = models.FileField(upload_to='./songs/mp3/', validators=[FileExtensionValidator(allowed_extensions=['mp3', 'wav', 'wma', 'amr'])])
    joinDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.song_name