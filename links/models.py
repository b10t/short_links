from django.db import models


class Links(models.Model):
    link = models.CharField(
        max_length=300,
        verbose_name='Ссылка')
    short_link = models.CharField(
        max_length=300,
        verbose_name='Короткая ссылка')

    def __str__(self) -> str:
        return f'{self.link}'

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'
