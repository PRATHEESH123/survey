from rest_framework import serializers
from django.core.exceptions import ValidationError

# local
from ..models import MultipleChoiceAnswer, Question


class MultipleChoiceAnswerSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = MultipleChoiceAnswer
        fields = (
            'user',
            'question',
            'answer',
        )
    def validate_answer(self, answer):
        question = Question.objects.filter(id =self.initial_data['question']).first()
        if set(answer).issubset(set(list(question.choice_set.all()))):
            return answer      
        else:
            raise ValidationError("Invalid choice for question:{}".format(self.initial_data['question']))
    
            
    def create(self, validated_data):
        answer, created = MultipleChoiceAnswer.objects.update_or_create(
            question=validated_data.get('question'),
            user=validated_data.get('user'),
            defaults={},
        )
        answer.answer.set(validated_data.get('answer'))
        return answer