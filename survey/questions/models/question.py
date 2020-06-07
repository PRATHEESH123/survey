from django.db import models


class Question(models.Model):
    """Model definition for Question."""

    title_text = models.CharField('Question Title', max_length=100)
    multiple = models.BooleanField(default= False)
    mandatory = models.BooleanField(default=False)
    

    class Meta:
        """Meta definition for Question."""

        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    def __str__(self):
        """Unicode representation of Question."""
        return f'{self.title_text}'