from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=255, verbose_name='Adı')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tip'
        verbose_name_plural = 'Tip'


class Room(models.Model):
    name = models.CharField(max_length=10, verbose_name='Oda tipi', help_text='örnek 1+1, 2+1')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Oda'
        verbose_name_plural = 'Oda'


class HeatType(models.Model):
    name = models.CharField(max_length=255, verbose_name='Tip', help_text='Örnek:  Doğalgaz (Kombi)')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Isıtma Tipi'
        verbose_name_plural = 'Isıtma Tipleri'


class Project(models.Model):
    name = models.CharField(verbose_name='Adı', max_length=255)
    main_image = models.ImageField(verbose_name='Resim', upload_to='projects/main_image/')
    description = models.TextField(verbose_name='Açıklama')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Proje'
        verbose_name_plural = 'Projeler'


class PropertyTitle(models.Model):
    title = models.CharField(max_length=255, verbose_name='Başlık', help_text='örnek: Cephe, Ulaşım')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Özellik Başlığı'
        verbose_name_plural = 'Özellik Başlıkları'


class Property(models.Model):
    title = models.ForeignKey(PropertyTitle, verbose_name='Ana Başlık', on_delete=models.CASCADE,
                              related_name='properties')
    name = models.CharField(max_length=255, verbose_name='Özellik')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Özellik'
        verbose_name_plural = 'Özellikler'


class Advert(models.Model):
    title = models.CharField(max_length=255, verbose_name='Başlık')
    image_detail = models.ImageField(verbose_name='Detay Sayfası İçin Resim', upload_to='advert/galeri/')
    image_list = models.ImageField(verbose_name='Listeleme Sayfası İçin Resim', upload_to='advert/galeri/')
    published_date = models.DateTimeField(verbose_name='Yayınlanma Tarihi')
    price = models.PositiveSmallIntegerField(verbose_name='Ücret')
    type = models.ForeignKey(Type, verbose_name='Tipi', on_delete=models.PROTECT, related_name='adverts')
    square = models.PositiveSmallIntegerField(verbose_name='m² (Brüt)')
    square_useful = models.PositiveSmallIntegerField(verbose_name='m² (Net)')
    room = models.ForeignKey(Room, verbose_name='Oda Sayısı', on_delete=models.PROTECT, related_name='adverts')
    heating = models.ForeignKey(HeatType, verbose_name='Isınma', on_delete=models.PROTECT, related_name='adverts')
    bathroom_count = models.PositiveSmallIntegerField(verbose_name='Banyo Sayısı')
    is_furniture = models.BooleanField(verbose_name='Eşyalı')
    status = models.CharField(max_length=255, verbose_name='Kullanım Durumu')
    in_site = models.BooleanField(verbose_name='Site İçerisinde')
    project = models.ForeignKey(Project, verbose_name='Proje', on_delete=models.PROTECT, related_name='adverts',
                                null=True, blank=True)
    dues = models.PositiveSmallIntegerField(verbose_name='Aidat', null=True, blank=True)
    apartment_age = models.PositiveSmallIntegerField(verbose_name='Apartman Yaşı')
    content = models.TextField(verbose_name='Açıklama')
    coordinates = models.CharField(verbose_name='Konum', max_length=25, help_text='örnek: 56.545454, 59.32454')
    quarter = models.ForeignKey('address.Quarter', verbose_name='mahalle', on_delete=models.PROTECT,
                                related_name='adverts')
    properties = models.ManyToManyField(Property, verbose_name='Özellikleri', related_name='adverts')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'İlan'
        verbose_name_plural = 'İlanlar'


class AdvertImage(models.Model):
    advert = models.ForeignKey(Advert, verbose_name='İlan', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(verbose_name='Resim', upload_to='advert/galeri/')

    def __str__(self):
        return f'{self.id} {self.advert.title}'

    class Meta:
        verbose_name = 'Galeri'
        verbose_name_plural = 'Galeri'
