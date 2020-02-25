from django.db import models

from core.base_object_mixin import BaseObjectMixin
from education.models.homework import Homework


class Mark(BaseObjectMixin):
    value = models.PositiveIntegerField(default=100)
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return 'Task: ' + str(self.homework.home_task.name) + ' Mark: ' + str(self.value) + ' Student: ' + \
               str(self.homework.student.username)

    def save(self, *args, **kwargs):
        if self.value > self.homework.home_task.max_mark:
            raise ValueError('Value cannot be greater than the max mark of home task.')
        else:
            super(Mark, self).save()
