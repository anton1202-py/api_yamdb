from django.db import models
from users.models import User


SCORE_FOR_REVIEW = (
    (1, 1), (6, 6),
    (2, 2), (7, 7),
    (3, 3), (8, 8),
    (4, 4), (9, 9),
    (5, 5), (10, 10))


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
    name = models.TextField(max_length=50, verbose_name='name')
    year = models.IntegerField('Год создания')
    description = models.TextField(max_length=200, null=True, blank=True)
    genre = models.ManyToManyField(Genre)
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 related_name='titles', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Title'
        verbose_name_plural = 'Titles'


class Review(models.Model):
    title = models.ForeignKey(
        'Title', on_delete=models.CASCADE, related_name="reviews")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField(
        verbose_name='Текст отзыва', help_text='Напишите отзыв')
    score = models.IntegerField(
        help_text='Оцените произведение',
        choices=SCORE_FOR_REVIEW)
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
        Review, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    pub_date = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text
