from django.db import models
from django.core.exceptions import ValidationError

class Card(models.Model):
    title = models.CharField(max_length=200, verbose_name='Тема', help_text='Тема карточки обязательна.', blank=False)
    content_url = models.URLField(blank=True, null=True, verbose_name='Ссылка на содержимое')
    content_file = models.FileField(upload_to='card_files/', blank=True, null=True, verbose_name='Файл содержимого')

    def __str__(self):
        return self.title

    def clean(self):
        if not self.content_url and not self.content_file:
            raise ValidationError('Необходимо добавить содержимое: либо ссылку, либо документ.')
        if self.content_url and self.content_file:
            raise ValidationError('Добавьте только один тип содержимого: либо ссылку, либо документ.')
