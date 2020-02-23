from django.db import models
from django.utils.text import slugify

from core.base_object_mixin import BaseObjectMixin
from education.models.lecture import Lecture


class HomeTask(BaseObjectMixin):
    name = models.CharField(max_length=30)
    slug = models.SlugField()
    condition = models.TextField()
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(HomeTask, self).save(*args, **kwargs)
