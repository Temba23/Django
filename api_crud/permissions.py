from rest_framework.permissions import BasePermission
from django.contrib.auth.models import User


class IsSuperAdminUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        UserGroup = User.groups.through
        return UserGroup.objects.filter(user=request.user, group__name="admin").exist()

    # def has_permission(self, request, view):
    #     user_groups = request.user.groups.all().values_list('name', flat=True)
    #     return "Admin" in user_groups
class IsStudentUser(BasePermission):
    def has_permission(self, request, view):
        UserGroup = User.groups.through
        return UserGroup.objects.filter(user=request.user, group__name="student").exist()

class IsTutorUser(BasePermission):
    def has_permission(self, request, view):
        UserGroup = User.groups.through
        return UserGroup.objects.filter(user=request.user, group__name="tutor").exist()