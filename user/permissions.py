from rest_framework.permissions import BasePermission
class Update_Own_Credentials (BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == "GET":
            return True
        return obj.id == request.user.id
