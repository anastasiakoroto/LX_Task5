from rest_framework.permissions import BasePermission


class AllowActionToStudent(BasePermission):

    def has_permission(self, request, view):
        return request.user.student_user is True


class AllowActionToProfessor(BasePermission):

    def has_permission(self, request, view):
        return request.user.professor_user is True


class AllowActionToAllRoles(BasePermission):

    def has_permission(self, request, view):
        return request.user.professor_user is True or request.user.student_user is True
