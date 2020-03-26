from django.test import TestCase
from .models import Quiz
from web_scrap.models import Toolkit

class QuizTestCase(TestCase):
    def setUp(self):
        testingToolkit = Toolkit.objects.create(name="testing", url="https://www.rcgp.org.uk/clinical-and-research/resources/toolkits/acute-kidney-injury-toolkit.aspx")
        Quiz.objects.create(
            question = "testing question",
            answer_1 = "testing 1",
            answer_2 = "testing 2",
            answer_3 = "testing 3",
            answer_4 = "testing 4",

            correct_answer = 2,
            toolkit = testingToolkit
        )

    def test_quiz(self):
        """Able to save quiz in database"""
        quiz = Quiz.objects.get(question="testing question")
        toolkit = Toolkit.objects.get(name="testing")
        self.assertEqual(quiz.correct_answer, 2) 