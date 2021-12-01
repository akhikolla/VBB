import factory
from django.utils import timezone
from vbb_backend.session.models import (
    Session,
    StudentSessionAssociation,
    MentorSessionAssociation,
)
from vbb_backend.program.tests.factories import (
    SlotFactory,
    ComputerFactory,
    StudentFactory,
    MentorFactory,
)


class SessionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Session

    slot = factory.SubFactory(SlotFactory)
    computer = factory.SubFactory(ComputerFactory)
    start = factory.Faker("date_time", tzinfo=timezone.utc)
    end = factory.Faker("date_time", tzinfo=timezone.utc)


class StudentSessionAssociationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = StudentSessionAssociation

    student = factory.SubFactory(StudentFactory)
    session = factory.SubFactory(SessionFactory)


class MentorSessionAssociationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = MentorSessionAssociation

    mentor = factory.SubFactory(MentorFactory)
    session = factory.SubFactory(SessionFactory)


class SessionMentorStudentFactory(
    MentorSessionAssociationFactory, StudentSessionAssociationFactory
):
    mentor_session = factory.RelatedFactory(
        MentorSessionAssociationFactory,
        factory_related_name="session",
    )
    student_session = factory.RelatedFactory(
        StudentSessionAssociationFactory,
        factory_related_name="session",
    )
