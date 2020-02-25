from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    student_user = models.BooleanField(default=False)
    professor_user = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.student_user is True and self.professor_user is True:
            raise ValueError('You can choose only one role: student OR professor')
        else:
            super(User, self).save()
