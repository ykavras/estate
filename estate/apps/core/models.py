from django.db import models


class Test(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')

    class Meta:
        verbose_name = 'Test'
        verbose_name_plural = "Test Model"

    def __str__(self):
        return self.title
