from django.db import models
from django.contrib.auth import get_user_model


class MultipleChoiceAnswer(models.Model):
    """Model definition for MultipleChoiceAnswer."""

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    answer = models.ManyToManyField('Choice', null =True, blank = True)

    class Meta:
        """Meta definition for MultipleChoiceAnswer."""

        verbose_name = 'Multiple Choice Answer'
        verbose_name_plural = 'Multiple Choice Answers'

    def __str__(self):
        """Unicode representation of MultipleChoiceAnswer."""
        return f'{self.answer}'