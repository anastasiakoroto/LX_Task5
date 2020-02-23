from rest_framework import serializers

from education.models.comment import Comment
from education.models.course import Course
from education.models.hometask import HomeTask
from education.models.homework import Homework
from education.models.lecture import Lecture
from education.models.mark import Mark


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        exclude = ('slug',)


class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        exclude = ('slug',)


class HomeTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeTask
        exclude = ('slug',)


class HomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = '__all__'


class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mark
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
