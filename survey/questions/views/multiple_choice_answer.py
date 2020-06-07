from rest_framework import viewsets
from rest_framework import mixins

from ..serializers import MultipleChoiceAnswerSerializer
from ..models import MultipleChoiceAnswer


class MultipleChoiceAnswerViewset(viewsets.ModelViewSet):
    queryset = MultipleChoiceAnswer.objects.all()
    serializer_class = MultipleChoiceAnswerSerializer