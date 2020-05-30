from django.db import models


class Bb(models.Model):
    """Объявления"""
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    content = models.TextField(null=True, blank=True, verbose_name='Текст объявления')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        """Вид в админке"""
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ('published', 'title',)
