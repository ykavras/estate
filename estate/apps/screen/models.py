from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Panorama(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='panoramas')
    fade_duration = models.PositiveSmallIntegerField(verbose_name='Karartma Süresi(sn)')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return ''

    class Meta:
        verbose_name = 'Panorama'
        verbose_name_plural = 'Panoramas'


class Screen(models.Model):
    panorama = models.ForeignKey(Panorama,on_delete=models.CASCADE, related_name='screens')
    name = models.CharField(verbose_name='Screen ID', max_length=50)
    title = models.CharField(verbose_name='title', max_length=255)
    hfov = models.FloatField(verbose_name='hfov')
    pitch = models.FloatField(verbose_name='pitch')
    yaw = models.FloatField(verbose_name='yaw')
    northOffset = models.PositiveSmallIntegerField(verbose_name='northOffset')
    order = models.PositiveSmallIntegerField(verbose_name='Order')
    image = models.ImageField(upload_to='panorama-screens/')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return ''

    class Meta:
        verbose_name = 'Screen'
        verbose_name_plural = 'Screens'
        ordering = ('order',)


class HotSpot(models.Model):
    type = (('info', 'info'), ('scene', 'scene'))
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE, related_name='hotspots')
    text = models.CharField(max_length=255)
    pitch = models.FloatField()
    yaw = models.FloatField()
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return ''

    class Meta:
        verbose_name = 'HotSpot'
        verbose_name_plural = 'HotSpots'
