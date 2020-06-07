from django.db import models

class Choice(models.Model):

    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    choice_text = models.CharField('choice text', max_length=100)

    class Meta:
        """Meta definition for Choice."""

        verbose_name = 'Choice'
        verbose_name_plural = 'Choices'

    def __str__(self):
        """Unicode representation of Choice."""
        return f'{self.choice_text}'