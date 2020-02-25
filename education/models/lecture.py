from django.conf import settings
from django.db import models
from django.utils.text import slugify

from core.base_object_mixin import BaseObjectMixin
from education.models.course import Course


def file_path(instance, file_name):
    return f"uploads/lectures/{instance.course}/{instance.author.username}/{instance.name}/{file_name}"


class Lecture(BaseObjectMixin):
    name = models.CharField(max_length=80)
    slug = models.SlugField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               limit_choices_to={'professor_user': True})
    content = models.FileField(upload_to=file_path)
    course = models.ForeignKey(Course,
                               blank=True,
                               on_delete=models.CASCADE,
                               related_name='lecture')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Lecture, self).save(*args, **kwargs)
