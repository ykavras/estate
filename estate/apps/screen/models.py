from django.db import models
from django.shortcuts import reverse


class Screen(models.Model):
    advert = models.ForeignKey('advert.Advert', on_delete=models.CASCADE, related_name='screens')
    name = models.CharField(verbose_name='Screen ID', max_length=50, null=True, blank=True)
    title = models.CharField(verbose_name='title', max_length=255)
    hfov = models.CharField(max_length=255, verbose_name='hfov', null=True, blank=True)
    pitch = models.CharField(max_length=255, verbose_name='pitch', null=True, blank=True)
    yaw = models.CharField(max_length=255, verbose_name='yaw', null=True, blank=True)
    northOffset = models.PositiveSmallIntegerField(verbose_name='northOffset', null=True, blank=True)
    order = models.PositiveSmallIntegerField(verbose_name='Order', null=True, blank=True)
    image = models.ImageField(upload_to='panorama-screens/')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Screen, self).save(*args, **kwargs)
        if not self.order:
            self.order = self.pk
            return self.save()

    def get_absolute_url(self):
        return reverse('reverse:reverse', args=self.pk)

    def scene_hotspots(self):
        return self.hotspots.filter(type='scene')

    class Meta:
        verbose_name = 'Screen'
        verbose_name_plural = 'Screens'
        ordering = ('order',)


class HotSpot(models.Model):
    type_choices = (('info', 'info'), ('scene', 'scene'))
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE, related_name='hotspots',
                               help_text='Hangi ekranda gösterilecek')
    target_screen = models.ForeignKey(Screen, on_delete=models.CASCADE, related_name='my_links',
                                      verbose_name='Hedef Ekran', help_text='Sadece tip "scene" ise doldurunuz',
                                      null=True, blank=True)
    pitch = models.CharField(max_length=255, verbose_name="pitch")
    yaw = models.CharField(max_length=255, verbose_name="yaw")
    type = models.CharField(verbose_name='Types', max_length=5, choices=type_choices, null=True, blank=True, )
    text = models.CharField(max_length=255, null=True, blank=True, help_text='If type is info fill here')
    url = models.URLField(null=True, blank=True, help_text='If type is info then you may give link')

    def __str__(self):
        return self.text

    def costum_screen_id(self):
        return self.target_screen.name if self.target_screen else self.screen.name

    class Meta:
        verbose_name = 'HotSpot'
        verbose_name_plural = 'HotSpots'
