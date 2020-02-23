from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter

from education.api.serializers import (CourseSerializer,
                                       HomeTaskSerializer,
                                       HomeworkSerializer,
                                       LectureSerializer, MarkSerializer, CommentSerializer)
from education.models.comment import Comment
from education.models.course import Course
from education.models.hometask import HomeTask
from education.models.homework import Homework
from education.models.lecture import Lecture
from education.models.mark import Mark


class CourseViewSet(viewsets.ModelViewSet):
    http_method_names = ('get', 'post', 'put', 'delete')
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = (OrderingFilter, DjangoFilterBackend)
    filterset_fields = ('owner',)
    ordering_fields = ('created_at', 'name',)


class HomeTaskViewSet(viewsets.ModelViewSet):
    http_method_names = ('get', 'post', 'put', 'delete')
    queryset = HomeTask.objects.all()
    serializer_class = HomeTaskSerializer


class HomeworkViewSet(viewsets.ModelViewSet):
    http_method_names = ('get', 'post', 'put', 'delete')
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer
    filter_backends = (OrderingFilter,)
    ordering_fields = ('created_at', 'student')
    filterset_fields = ('status',)


class LectureViewSet(viewsets.ModelViewSet):
    http_method_names = ('get', 'post', 'put', 'delete')
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
    filter_backends = (OrderingFilter, DjangoFilterBackend)
    ordering_fields = ('created_at', 'name')
    filterset_fields = ('course',)


class MarkViewSet(viewsets.ModelViewSet):
    http_method_names = ('get', 'post', 'put', 'delete')
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer
    filter_backends = (OrderingFilter,)
    ordering_fields = ('value',)


class CommentViewSet(viewsets.ModelViewSet):
    http_method_names = ('get', 'post', 'put', 'delete')
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = (OrderingFilter,)
    ordering_fields = ('created_at',)
