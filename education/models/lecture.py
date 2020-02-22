from django.db import models
from django.utils.text import slugify
from django.utils.timezone import now as tz_now

from core.base_object_mixin import BaseObjectMixin


def file_path(instance, file_name):
    now = tz_now()
    return f"uploads/lectures/{now.year}/{now.month}/{now.day}/{file_name}"


class Lecture(BaseObjectMixin):
    name = models.CharField(max_length=80)
    slug = models.SlugField()
    content = models.FileField(upload_to=file_path)
    # home_task = models.ForeignKey(HomeTask, on_delete=models.CASCADE)  # ???

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Lecture, self).save(*args, **kwargs)
