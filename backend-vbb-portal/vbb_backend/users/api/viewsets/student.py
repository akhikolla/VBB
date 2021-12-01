from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from vbb_backend.users.api.serializers.student import StudentSerializer
from vbb_backend.program.models import School
from vbb_backend.users.models import Student
from vbb_backend.users.models import UserTypeEnum


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = StudentSerializer
    lookup_field = "external_id"

    def get_queryset(self):
        queryset = self.queryset.filter(user__user_type=UserTypeEnum.STUDENT.value)
        user = self.request.user
        school = self.get_school()
        queryset = queryset.filter(school=school)
        if user.is_superuser:
            pass
        elif user.user_type in [UserTypeEnum.HEADMASTER.value]:
            queryset = queryset.filter(school__program__program_director=user)
        else:
            raise PermissionDenied()
        return queryset

    def get_school_post(self):
        return get_object_or_404(School, external_id=self.request.data.get("school"))

    def get_school(self):
        return get_object_or_404(School, external_id=self.request.GET.get("school"))

    def perform_create(self, serializer):
        serializer.save(school=self.get_school_post())
