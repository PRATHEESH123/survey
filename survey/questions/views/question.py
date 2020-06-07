from rest_framework import viewsets
from rest_framework import mixins

from ..serializers import QuestionSerializer
from ..models import Question


class QuestionViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
