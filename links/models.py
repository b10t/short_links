from random import choice, shuffle
from string import ascii_letters, digits

from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.db import models


class Links(models.Model):
    link = models.URLField(
        max_length=300,
        validators=[URLValidator()],
        verbose_name='Ссылка')
    link_id = models.CharField(
        max_length=300,
        blank=True,
        verbose_name='Идентификатор ссылки')

    def __str__(self) -> str:
        return f'{self.link}'

    def save(self, *args, **kwargs):
        try:
            URLValidator()(self.link)
        except ValidationError as e:
            raise ValidationError(e)

        if not self.link_id:
            self.link_id = self.generate_link_id()
        super().save(*args, **kwargs)

    @staticmethod
    def generate_link_id(length_id=6):
        chars = list(ascii_letters)
        chars.extend(list(digits))
        shuffle(chars)

        return ''.join([choice(chars) for _ in range(length_id)])

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'
