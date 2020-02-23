from django.db import models

from core.base_object_mixin import BaseObjectMixin
from education.models.hometask import HomeTask
from education.models.homework import Homework


class Mark(BaseObjectMixin):
    value = models.PositiveIntegerField(default=100)
    # home_task = models.ForeignKey(HomeTask, on_delete=models.CASCADE, default=0)
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return 'Task: ' + str(self.homework.home_task.name) + '. Mark: ' + str(self.value) + '. Student: ' + \
               str(self.homework.student.username)
