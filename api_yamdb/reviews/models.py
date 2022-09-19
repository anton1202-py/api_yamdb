from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from users.models import User
from .validators import validate_max_year


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='name')
    slug = models.SlugField(unique=True, verbose_name='slug')

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'


class Genre(models.Model):
    name = models.CharField(max_length=30, verbose_name='name')
    slug = models.SlugField(unique=True, verbose_name='slug')

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'


class Title(models.Model):
    name = models.CharField(
        max_length=500,
        verbose_name='Название'
    )
    description = models.TextField(
        max_length=10000,
        verbose_name='Описание',
        null=True,
        blank=True
    )
    year = models.IntegerField(
        verbose_name='Год выпуска', validators=[validate_max_year])
    genre = models.ManyToManyField(
        Genre,
        through='TitleGenre',
        verbose_name='Жанр',
    )
    category = models.ForeignKey(
        Category,
        related_name="titles",
        verbose_name="Категория",
        null=True,
        on_delete=models.SET_NULL
    )

    class Meta:
        verbose_name = 'Произведение'

    def __str__(self):
        return self.name


class TitleGenre(models.Model):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.title} {self.genre}'


class Review(models.Model):
    title = models.ForeignKey(
        'Title', on_delete=models.CASCADE, related_name="reviews")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField(
        verbose_name='Текст отзыва', help_text='Напишите отзыв')
    score = models.SmallIntegerField(
        help_text='Оцените произведение от 1 до 10',
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ])
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'title'],
                name='unique review')
        ]
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.text


class Comment(models.Model):
    text = models.TextField(
        verbose_name='Текст комментария',
        help_text='Напишите комментарий'
    )
    review = models.ForeignKey(
        Review,
        blank=True, null=True,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    pub_date = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text
