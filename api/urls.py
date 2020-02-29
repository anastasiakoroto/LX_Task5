from django.urls import include, path
from rest_framework import routers

from account.views import UserViewSet
from education.api.views import (CommentViewSet,
                                 CourseViewSet,
                                 HomeTaskViewSet,
                                 HomeworkViewSet,
                                 LectureViewSet,
                                 MarkViewSet)


router = routers.DefaultRouter()
router.register(r'course', CourseViewSet)
router.register(r'home-task', HomeTaskViewSet)
router.register(r'homework', HomeworkViewSet)
router.register(r'lecture', LectureViewSet)
router.register(r'mark', MarkViewSet)
router.register(r'comment', CommentViewSet)

router.register(r'user', UserViewSet)
urlpatterns = [
    path(r'', include(router.urls)),
    path(r'api/auth', include('rest_framework.urls'))
]
