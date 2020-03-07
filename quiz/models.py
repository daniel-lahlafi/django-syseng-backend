from django.db import models
from web_scrap.models import Toolkit 

class Quiz(models.Model):
    def __str__(self):
        return 'Question: {0} | Toolkit: {1}'.format(
            self.question,
            self.toolkit.name)

    question = models.TextField()
    answer_1 = models.TextField()
    answer_2 = models.TextField()
    answer_3 = models.TextField()
    answer_4 = models.TextField()
    CHOICES = [
        (1,'Answer 1'),
        (2,'Answer 2'),
        (3,'Answer 3'),
        (4,'Answer 4'),
    ]
    correct_answer = models.IntegerField(choices=CHOICES)
    toolkit = models.ForeignKey(Toolkit, on_delete=models.CASCADE)
