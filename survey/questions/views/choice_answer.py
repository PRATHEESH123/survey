from rest_framework import viewsets
from rest_framework import mixins

from ..serializers import ChoiceAnswerSerializer
from ..models import ChoiceAnswer


class ChoiceAnswerViewset(viewsets.ModelViewSet):
    queryset = ChoiceAnswer.objects.all()
    serializer_class = ChoiceAnswerSerializer