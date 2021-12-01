import enum

from django.db import models


class QuestionareQuestions(models.Model):
    class AnswerTypeEnum(enum.Enum):
        INTEGER = 1
        DECIMAL = 2
        DATETIME = 3
        TEXT = 4

    AnswerTypeChoices = [(e.value, e.name) for e in AnswerTypeEnum]

    question = models.TextField(null=False, blank=False)
    question_tag = models.CharField(max_length=255)
    expected_answer_type = models.IntegerField(
        choices=AnswerTypeChoices, default=AnswerTypeEnum.TEXT.value
    )

    class Meta:
        abstract = True


class QuestionareAnswers(models.Model):
    answer = models.TextField(null=False, blank=False)

    class Meta:
        abstract = True