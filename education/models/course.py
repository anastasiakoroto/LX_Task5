from django.conf import settings
from django.db import models
from django.utils.text import slugify

from core.base_object_mixin import BaseObjectMixin


class Course(BaseObjectMixin):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              limit_choices_to={'professor_user': True})
    professor = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                       blank=True,
                                       related_name='course_p',  # rename
                                       limit_choices_to={'professor_user': True})
    student = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                     blank=True,
                                     related_name='course_s',  # rename
                                     limit_choices_to={'student_user': True})

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Course, self).save(*args, **kwargs)
