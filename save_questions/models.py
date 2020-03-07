from django.db import models

# Create your models here.
class Question(models.Model):
    def __str__(self):
        return "Question: {0}, Toolkit: {1}, Answer: {2}".format(
            self.question,
            self.toolkit,
            self.answer
        )
    
    question = models.CharField(max_length=256, unique=True)
    toolkit = models.CharField(max_length=256)
    answer = models.CharField(max_length=256)
