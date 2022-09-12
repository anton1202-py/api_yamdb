from django.db.models import Avg
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status, viewsets
from rest_framework.response import Response
from reviews.models import Category, Genre, Review, Title

from .filters import ModelFilter
from .permissions import AdminModerator, GeneralPrmission
from .serializers import (CategoriesSerializer, CommentSerializer,
                          GenreSerializer, ReviewSerializer,
                          TitleGeneralSerializer, TitleSlugSerializer)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (AdminModerator,)

    def get_queryset(self):
        title_id = self.kwargs.get('title_id')
        title = get_object_or_404(Title, id=title_id)
        return title.reviews.all()

    def perform_create(self, serializer):
        title_id = self.kwargs.get('title_id')
        title = get_object_or_404(Title, id=title_id)
        serializer.save(author=self.request.user, title=title)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (AdminModerator,)

    def get_queryset(self):
        review_id = self.kwargs.get('review_id')
        review = get_object_or_404(Review, id=review_id)
        return review.comments.all()

    def perform_create(self, serializer):
        review_id = self.kwargs.get('review_id')
        review = get_object_or_404(Review, id=review_id)
        serializer.save(author=self.request.user, review=review)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    lookup_field = 'slug'
    serializer_class = GenreSerializer
    permission_classes = [GeneralPrmission]
    filter_backends = [filters.SearchFilter]
    search_fields = ('name',)

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    lookup_field = 'slug'
    serializer_class = CategoriesSerializer
    permission_classes = [GeneralPrmission]

    filter_backends = [filters.SearchFilter]
    search_fields = ('name',)

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class TitleViewSet(viewsets.ModelViewSet):
    filter_backends = (DjangoFilterBackend,)
    filter_class = ModelFilter
    permission_classes = [GeneralPrmission]

    def get_serializer_class(self):
        if self.action in ('create', 'partial_update'):
            return TitleSlugSerializer
        return TitleGeneralSerializer

    def get_queryset(self):
        return Title.objects.all().annotate(rating=Avg('reviews__score'))
