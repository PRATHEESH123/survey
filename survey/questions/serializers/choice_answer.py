from rest_framework import serializers
from django.core.exceptions import ValidationError
# local
from ..models import ChoiceAnswer, Question


class ChoiceAnswerSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = ChoiceAnswer
        fields = (
            'user',
            'question',
            'answer',
        )

    def validate_answer(self, answer):
        question = Question.objects.filter(id =self.initial_data['question']).first()
        if answer is not None:
            if str(self.initial_data['question']) == str(answer.question.id):
                return answer
            else:
                raise ValidationError("Invalid choice for question:{}".format(self.initial_data['question']))
        else:
            if question.mandatory is True:
                raise ValidationError("missing required field".format(self.initial_data['question']))
            else:
                # if str(self.initial_data['question']) == str(answer.question.id):
                return answer
                # else:
                #     raise ValidationError("Invalid choice for question:{}".format(self.initial_data['question']))

    def create(self, validated_data):
        answer, created = ChoiceAnswer.objects.update_or_create(
            question=validated_data.get('question'),
            user=validated_data.get('user'),
            defaults={'answer': validated_data.get('answer')}
        )
        return answer
