from django.db import models


class Station(models.Model):
    title = models.CharField('Название', max_length=50)
    station = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Станция'
        verbose_name_plural = 'Станции'
