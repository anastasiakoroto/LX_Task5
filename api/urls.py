from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from rest_framework import routers

from education.api.views import (CourseViewSet,
                                 HomeTaskViewSet,
                                 HomeworkViewSet,
                                 LectureViewSet)


router = routers.DefaultRouter()
router.register(r'course', CourseViewSet)
router.register(r'home-task', HomeTaskViewSet)
router.register(r'homework', HomeworkViewSet)
router.register(r'lecture', LectureViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
]
