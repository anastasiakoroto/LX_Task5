from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

from core.base_object_mixin import BaseObjectMixin


class Course(BaseObjectMixin):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    professor = models.ManyToManyField(User, blank=True, related_name='course_p')
    student = models.ManyToManyField(User, blank=True, related_name='course_s')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Course, self).save(*args, **kwargs)
