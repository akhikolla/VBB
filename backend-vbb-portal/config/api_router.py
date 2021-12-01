from django.conf import settings
from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework_nested.routers import NestedSimpleRouter

from vbb_backend.program.api.viewsets.classroom import ClassroomViewSet
from vbb_backend.program.api.viewsets.computer import ComputerViewSet
from vbb_backend.program.api.viewsets.program import ProgramViewSet
from vbb_backend.program.api.viewsets.school import SchoolViewSet
from vbb_backend.program.api.viewsets.slot import SlotViewSet
from vbb_backend.program.api.viewsets.slotMentor import (
    MentorBookingViewSet,
    MentorSlotViewSet,
)
from vbb_backend.program.api.viewsets.slotStudent import StudentSlotViewSet
from vbb_backend.session.api.viewsets.session import SessionViewSet
from vbb_backend.session.api.viewsets.sessionMentor import MentorSessionViewSet
from vbb_backend.session.api.viewsets.sessionStudent import StudentSessionViewSet
from vbb_backend.users.api.viewsets.newsletter import NewsletterSubscriberViewSet
from vbb_backend.users.api.viewsets.student import StudentViewSet
from vbb_backend.users.api.viewsets.mentor import MentorViewSet
from vbb_backend.users.api.viewsets.teacher import TeacherViewSet
from vbb_backend.users.api.viewsets.program_director import ProgramDirectorViewSet
from vbb_backend.users.api.viewsets.program_manager import ProgramManagerViewSet
from vbb_backend.users.api.viewsets.headmaster import HeadmasterViewSet
from vbb_backend.users.api.viewsets.parent import ParentViewSet
from vbb_backend.users.api.viewsets.executive import ExecutiveViewSet
from vbb_backend.users.api.viewsets.mentorNoAuth import MentorNoAuthViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("newsletter", NewsletterSubscriberViewSet)

router.register("mentor", MentorViewSet)
router.register("teacher", TeacherViewSet)
router.register("programDirector", ProgramDirectorViewSet)
router.register("programManager", ProgramManagerViewSet)
router.register("headmaster", HeadmasterViewSet)
router.register("parent", ParentViewSet)
router.register("executive", ExecutiveViewSet)

if not settings.IS_PRODUCTION:
    router.register("mentorNoAuth", MentorNoAuthViewSet)

router.register("session", SessionViewSet)

session_nested_router = NestedSimpleRouter(router, r"session", lookup="session")

session_nested_router.register("mentor", MentorSessionViewSet)
session_nested_router.register("student", StudentSessionViewSet)


router.register("slot", SlotViewSet)

slot_nested_router = NestedSimpleRouter(router, r"slot", lookup="slot")

slot_nested_router.register(r"student", StudentSlotViewSet)

slot_nested_router.register(r"mentor", MentorSlotViewSet)


router.register("program", ProgramViewSet)

program_nested_router = NestedSimpleRouter(router, r"program", lookup="program")

router.register("computer", ComputerViewSet)

router.register(r"school", SchoolViewSet)


school_nested_router = program_nested_router

router.register(r"classroom", ClassroomViewSet)

school_nested_router.register(r"student", StudentViewSet)


app_name = "api"

urlpatterns = [
    url(r"^", include(router.urls)),
    url(r"^", include(program_nested_router.urls)),
    url(r"^", include(school_nested_router.urls)),
    url(r"^", include(slot_nested_router.urls)),
    url(r"^", include(session_nested_router.urls)),
]
