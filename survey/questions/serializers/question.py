from rest_framework import serializers

# local
from ..models import Question
from .choice import ChoiceSerializer


class QuestionSerializer(serializers.ModelSerializer):
    choice_set = ChoiceSerializer(many=True)
    # text_answer = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = (
            'id',
            'title_text',
            'multiple',
            'mandatory',
            'choice_set',
        )

    # def get_text_answer(self, instance):
    #     user = self.context.get('request').user

    #     if instance.type != instance.TEXT:
    #         return ''

    #     text_answer = instance.textanswer_set.filter(user=user).first()
    #     if not text_answer:
    #         return ''

    #     return text_answer.answer