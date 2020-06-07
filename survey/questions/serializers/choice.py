from rest_framework import serializers

# local
from ..models import Choice


class ChoiceSerializer(serializers.ModelSerializer):
    selected = serializers.SerializerMethodField()

    class Meta:
        model = Choice
        fields = (
            'id',
            'choice_text',
            'selected',
        )

    def get_selected(self, instance):
        user = self.context.get('request').user
        choice_answer = user.choiceanswer_set.filter(answer=instance).exists()
        multiple_choice_answer = user.multiplechoiceanswer_set.filter(answer=instance).exists()
        return choice_answer or multiple_choice_answer