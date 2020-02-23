from rest_framework import serializers

from education.models.course import Course
from education.models.hometask import HomeTask
from education.models.homework import Homework
from education.models.lecture import Lecture


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
