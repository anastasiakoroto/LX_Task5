from django.contrib import admin

# from education.models.comment import Comment
from education.models.course import Course
from education.models.hometask import HomeTask
from education.models.homework import Homework
from education.models.lecture import Lecture
# from education.models.mark import Mark

# Register your models here.
admin.site.register(Course)
# admin.site.register(Comment)
admin.site.register(HomeTask)
admin.site.register(Homework)
admin.site.register(Lecture)
# admin.site.register(Mark)
