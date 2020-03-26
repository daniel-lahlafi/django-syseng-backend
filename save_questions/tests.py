from django.test import TestCase
from .models import Question
from web_scrap.models import Toolkit

class QuestionTestCase(TestCase):
    def setUp(self):
        Toolkit.objects.create(name="testing", url="https://www.rcgp.org.uk/clinical-and-research/resources/toolkits/acute-kidney-injury-toolkit.aspx")
    def test_setting_question(self):
        """Able to save questions in database"""
        toolkit = Toolkit.objects.get(name="testing")
        Question.objects.create(
            question = "testing",
            toolkit = toolkit,
            answer = "answer"
        )
        question = Question.objects.get(question="testing")
        self.assertEqual(question.toolkit, Toolkit.objects.get(name="testing")) 
        self.assertEqual(question.answer, "answer")
