from django.db import models
from django.contrib.auth import get_user_model


class ChoiceAnswer(models.Model):
    """Model definition for ChoiceAnswer."""

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    answer = models.ForeignKey('Choice', on_delete=models.CASCADE, null=True)

    class Meta:
        """Meta definition for ChoiceAnswer."""

        verbose_name = 'Choice Answer'
        verbose_name_plural = 'Choice Answers'

    def __str__(self):
        """Unicode representation of ChoiceAnswer."""
        return f'{self.answer}'