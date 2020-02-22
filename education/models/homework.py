from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now as tz_now
from django.utils.translation import gettext
from enum import Enum


from core.base_object_mixin import BaseObjectMixin
from education.models.hometask import HomeTask


def file_path(instance, file_name):
    now = tz_now()
    return f'uploads/home_tasks/{instance.student}' \
           f'{instance.home_task}/{now.year}/{now.month}/{now.day}/{file_name}'


class HomeworkStatus(Enum):
    PASSED = 'PASSED'
    NOT_PASSED = 'NOT PASSED'


HOMEWORK_STATUS = ((HomeworkStatus.PASSED.value, gettext('Passed')),
                   (HomeworkStatus.NOT_PASSED, gettext('Not passed yet')))


class Homework(BaseObjectMixin):
    content = models.FileField(upload_to=file_path)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    home_task = models.ForeignKey(HomeTask, on_delete=models.CASCADE)
    status = models.CharField(choices=HOMEWORK_STATUS, max_length=20, default=HOMEWORK_STATUS[1])
    # mark = models.PositiveIntegerField(default=0)

    def __str__(self):
        return 'Home task: ' + str(self.home_task) + '. Student: ' + str(self.student)
