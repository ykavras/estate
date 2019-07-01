from django.db import models


class City(models.Model):
    name = models.CharField(verbose_name='Adı', max_length=255)
    code = models.CharField(verbose_name='Plaka kodu', max_length=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'İl'
        verbose_name_plural = 'İller'
        ordering = ('name',)


class District(models.Model):
    city = models.ForeignKey(City, verbose_name='İl', on_delete=models.CASCADE, related_name='districts')
    name = models.CharField(verbose_name='Adı', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'İlçe'
        verbose_name_plural = 'İlçeler'
        ordering = ('name',)


class Quarter(models.Model):
    district = models.ForeignKey(District, verbose_name='İlçe', on_delete=models.CASCADE, related_name='quarters')
    name = models.CharField(verbose_name='Adı', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Mahalle'
        verbose_name_plural = 'Mahalleler'
        ordering = ('name',)
