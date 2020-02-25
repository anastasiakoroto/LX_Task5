from django.conf import settings
from django.db import models

from core.base_object_mixin import BaseObjectMixin
from education.models.mark import Mark


class Comment(BaseObjectMixin):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    mark = models.ForeignKey(Mark, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
