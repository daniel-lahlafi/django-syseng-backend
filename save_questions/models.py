from django.db import models
from web_scrap.models import Toolkit

# Create your models here.
class Question(models.Model):
    def __str__(self):
        return "Question: {0}, Toolkit: {1}, Answer: {2}".format(
            self.question,
            self.toolkit.name,
            self.answer
        )
    
    question = models.CharField(max_length=256, unique=True)
    toolkit = models.ForeignKey(Toolkit, on_delete=models.CASCADE)
    answer = models.TextField(max_length=256)
