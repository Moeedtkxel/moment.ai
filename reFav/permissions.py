# from rest_framework import permissions
#
#
# class IsSuperUserOrOwner(permissions.BasePermission):
#     """
#     Custom permission to only superusers and owners of objects to edit it.
#     """
#
#     def has_object_permission(self, request, view, obj):
#         return request.user.is_superuser is True or obj.created_by == request.user
#
#
# class IsOwner(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request.user:
#             return obj == request.user
#         return False
#
#
# class IsSelfOrOrgAdminOrSuperUser(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         # Check whether user is accessing their data, or they are a super user or they are the org admin
#         return request.user == obj or request.user.is_superuser is True \
#                or (request.user.is_staff is True and request.user.organization == obj.organization)
#
#
# class IsSuperUserOrStaff(permissions.BasePermission):
#     """
#     Custom permission to only superusers and owners of objects to edit it.
#     """
#
#     def has_object_permission(self, request, view, obj):
#         return request.user.is_superuser is True or request.user.is_staff is True
