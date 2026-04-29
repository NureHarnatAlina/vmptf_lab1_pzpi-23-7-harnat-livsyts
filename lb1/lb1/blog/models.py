from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Назва',
    )
    description = models.TextField(
        blank=True,
        verbose_name='Опис',
    )

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'
        ordering = ['name']

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Назва',
    )
    content = models.TextField(
        verbose_name='Зміст',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='articles',
        verbose_name='Категорія',
    )
    published = models.BooleanField(
        default=True,
        verbose_name='Опубліковано',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Створено',
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Оновлено',
    )

    class Meta:
        verbose_name = 'Стаття'
        verbose_name_plural = 'Статті'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Стаття',
    )
    author = models.CharField(
        max_length=100,
        verbose_name='Автор',
    )
    text = models.TextField(
        verbose_name='Текст',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата коментування',
    )

    class Meta:
        verbose_name = 'Коментар'
        verbose_name_plural = 'Коментарі'
        ordering = ['created_at']

    def __str__(self):
        return f'{self.author}: {self.text[:30]}'
