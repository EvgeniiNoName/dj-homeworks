from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение', )
    scopes = models.ManyToManyField('Scope', through='ArticleScope')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Scope(models.Model):
    name = models.CharField(max_length=255)
    # is_main = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class ArticleScope(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    scope = models.ForeignKey('Scope', on_delete=models.CASCADE)
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.article.title} - {self.scope.name}'
