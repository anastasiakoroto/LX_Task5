from django.conf import settings
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
    NOT_PASSED = 'NOT_PASSED'


HOMEWORK_STATUS = ((HomeworkStatus.PASSED.value, gettext('Passed')),
                   (HomeworkStatus.NOT_PASSED.value, gettext('Not passed yet')))


class Homework(BaseObjectMixin):
    content = models.FileField(upload_to=file_path)
    student = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                limit_choices_to={'student_user': True})
    home_task = models.ForeignKey(HomeTask, on_delete=models.CASCADE)
    status = models.CharField(choices=HOMEWORK_STATUS,
                              max_length=100,
                              default=HOMEWORK_STATUS[1])

    class Meta:
        unique_together = ('student', 'home_task')

    def __str__(self):
        return 'Home task: ' + str(self.home_task.name) + '. Student: ' + str(self.student)
