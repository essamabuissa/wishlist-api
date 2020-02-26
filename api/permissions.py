from rest_framework.permissions import BasePermission
from items.models import Item

class StaffOrUser(BasePermission):
    def has_object_permission(self , request , view,obj):
        if request.user.is_staff or (request.user == obj.added_by):
            return True
        return False
