from django.db import models


class Screen(models.Model):
    advert = models.ForeignKey('advert.Advert', on_delete=models.CASCADE, related_name='screens')
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
    type_choices = (('info', 'info'), ('scene', 'scene'))
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE, related_name='hotspots')
    pitch = models.FloatField()
    yaw = models.FloatField()
    type = models.CharField(verbose_name='Types',max_length=5, choices=type_choices)
    text = models.CharField(max_length=255, null=True, blank=True, help_text='If type is info fill here')
    screenid = models.CharField(verbose_name='Screen Id', max_length=255, null=True, blank=True,
                                 help_text='If type is screen fill here')
    url = models.URLField(null=True, blank=True, help_text='If type is info then you may give link')

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return ''

    class Meta:
        verbose_name = 'HotSpot'
        verbose_name_plural = 'HotSpots'
